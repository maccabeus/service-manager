from api.models import Customer, WorkOrder, Service, AppSettings, Holiday
from api.library.utilities import Utilities
from api.library.employee import EmployeeManager
from api.serializers import WorkOrderSerializer, ServiceSerializer
from datetime import datetime, timedelta
import pytz

class WorkOrderManager:
    """
    Expose the necessary API to communicate with the  user scheduled work orders
    """
    formatter = None

    def search_order(request):

        email = request.GET.get('email')
        # the customer's email.

        service_id = request.GET.get('service_id')
        # optional service_id parameter. We will also use if provided

        if(email == None):
            """
            for each search request, the customer email must be provided
            """
            return Utilities.response_formatter(True, "email  must be provided")

        try:
            if(service_id) :
                orders = WorkOrder.objects.filter(service_id=service_id, customer_id=email)
            else:
                orders = WorkOrder.objects.filter(customer_id=email)

            """
            search service schedules using only the service_id
            this is the ``service_id`` previously issued to the customer
            """

            if(len(orders) <= 0):
                # if not work order found, return empty data
                return Utilities.response_formatter(False, "No work order found", [])

            serialized_orders = WorkOrderSerializer(orders, many=True)
            # serialize data and return
            return Utilities.response_formatter(False, "Work order found", serialized_orders.data)

        except:
            return Utilities.response_formatter(True, "Erro occurs. Please try again")
            """ an error occurs and we must retry"""

    def search_order_by_date_range(request):
        """
        Search work order using the date range provided. both ``date_from`` and ``date_to``
        must be provided for this to work as we search through the date ranges

        """

        email = request.GET.get('email')
        # the customer's email.
        date_from = request.GET.get('date_from')
        date_to = request.GET.get('date_to')

        service_id = request.GET.get('service_id')
        # if service_id is also provided, we will use as part of our data filter

        if(email == None):
            """
            for each search request, the customer email must be provided
            """
            return Utilities.response_formatter(True, "Email must be provided")

        if(date_from == None or date_to == None):
            """
            validate the date ranhes provided. Both must be available
            """
            return Utilities.response_formatter(True, "date_from and date_to must be provided")

        try:
            """
            search service schedules using only the email and date range provided
            """
            if(service_id != None):
                orders = WorkOrder.objects.filter(
                    date_created__range=[date_from, date_to], service_id=service_id)
                # filter also using the ``service_id```
            else:
                orders = WorkOrder.objects.filter(
                    date_created__range=[date_from, date_to])
                # select model using only the date_from and date_to

            if(len(orders) <= 0):
                # if not work order found, return empty data
                return Utilities.response_formatter(False, "No work order found for date range", [])

            serialized_orders = WorkOrderSerializer(orders, many=True)
            # serialize data and return
            return Utilities.response_formatter(False, "Work order found", serialized_orders.data)

        except:
            return Utilities.response_formatter(True, "Erro occurs. Please try again")
            """ an error occurs and we must retry"""

    def add_order(request):
        """
        Handles the addition creation of new service request. There are some valid consideration before a service request can be added:

        : The day cannot be ``Sunday``
        : Service request cannot be earlier than 9:00 AM and not later than 5:PM  (Mon- Saturday)
        : Service Request cannot be on an holiday. 

        :Note: we have updated some holidays in the holiday table

        """
        email = request.data.get('email')
        service_id = request.data.get('service_id')

        current_date_mock = request.data.get('current_date_mock')
        # value for date mocking . Use only when unit testing

        user_timezone = request.data.get('user_timezone')
        # if we provide timezone, this must be same with our orginization timezone
        # we could also convert other users timezones to our organization's time zone

        try:
            """  Get application settings. """
            app_settings = AppSettings.objects.all()

            if(len(app_settings) <= 0):
                # app at least one  settings must be defined for app to function
                return Utilities.response_formatter(True, "App settings not defined")
        except:
            return Utilities.response_formatter(True, "Error while loading App Settings")

        opening_hour = app_settings.filter(setting='opening_hour').values_list(
            'value', flat=True).first() or 9
        # schedule cannot be earlier than this opening hour. default to 9:00AM

        closing_hour = app_settings.filter(setting='closing_hour').values_list(
            'value', flat=True).first() or 17
        # schedule cannot be later than the closing hour.  default to 5:00PM

        app_timezone = app_settings.filter(setting='timezone').values_list(
            'value', flat=True).first() or 'UTC'
        # app timezone will be use while creating time slot for service

        if(email == None):
            """ validate inputs"""
            return Utilities.response_formatter(True, "email must be provided")

        if(service_id == None):
            return Utilities.response_formatter(True, "service_id must be provided")

        service_details = Service.objects.filter(id=service_id)
        """ if service details not found, we will stop execution and notify of error"""
        if(len(service_details) <= 0):
            return Utilities.response_formatter(True, "Service details not found. Please ensure you have prodived the correct service_id")
        
        if(current_date_mock!=None):
            current_date = datetime.fromisoformat(current_date_mock)
            # convert the mock date string to a date object. For test cases
        else:
            current_date = datetime.now()
        # use current date

        """ 
        we will utilize the server date for service request date consistency
        if timezone is provided, this timezone must be consistent with our app timezone

        if user timezone is different from app timezone, we must convert the user time to app timezone 
        equivalent
        """
        current_day = current_date.weekday()
        current_hour = current_date.hour

        if(current_day == 6):
            # we cannot schedule service request on a sunday
            return Utilities.response_formatter(error=True, message="Cannot schedule service request on Sunday")

        # used for testing current_hour=10
        if(current_hour < float(opening_hour)):
            """ for  every other weekdays, validate against the ``opening_hour`` and ``closing_hour`` """
            return Utilities.response_formatter(error=True, message="Cannot schedule earlier than {}:00AM".format(opening_hour))

        if(current_hour > float(closing_hour)):
            """ we cannot create service that is already beyond the closing_hour """
            return Utilities.response_formatter(error=True, message="Cannot schedule later than {}:00PM.".format(closing_hour))

        search_date = current_date.strftime('%Y-%m-%d')
        # format the date in to harmonize with our model format

        holiday = Holiday.objects.filter(date=search_date)
        # if there is an holiday, we cannot schedule work
        if(len(holiday) > 0):
            holiday_name = holiday.values_list(
                'description', flat=True).first()
            return Utilities.response_formatter(error=True, message="There is {} holiday on {} ".format(holiday_name, search_date))
           

        service_description = service_details.values_list(
            'name', flat=True).first()
        service_duration = service_details.values_list(
            'duration', flat=True).first()
        """
        get the description and service duration of the service requested. 
        Note: duration saved in the db is in minutes.
        """
        current_time_object = current_date+timedelta(seconds=1)
        current_time = current_time_object.strftime('%H:%M:%S')
        # string equivalent of current_time
        current_time_value = current_time.replace(':', '')
        # the number equivalent of our current _time. This value and the end_time_value will be use foe time comparism
        # while attempting to allocate or reallocate schedule slots for each request

        end_time_date_object = (
            current_date + timedelta(minutes=float(service_duration)))
        """ Note: service duration is always in minutes"""
        end_time = end_time_date_object.strftime('%H:%M:%S')

        end_date = end_time_date_object.strftime('%Y-%m-%d')
        # for services that spans beyond a day,we need to provide the end date from the date object

        end_time_value = end_time.replace(':', '')
        # the  number equivalent of our end_time

        # scheduled_order_list = WorkOrder.objects.filter(
        #     date_created=search_date, service_id=service_id, start_time_value__gte=current_time_value, done=0)

        scheduled_order_list = WorkOrder.objects.filter(
            date_created=search_date, service_id=service_id, done=0)
        # select all schedule for this service today.

        employee_id = EmployeeManager.get_available_employee_id()
        # get any free employee id to assign to this schedule order

        msg_no_slot="Oops! No time slot available again Please try later or tomorrow"

        if(len(scheduled_order_list) <= 0):

            if(Utilities.is_slot_within_closing_hour(closing_hour=closing_hour, slot_end_time=end_time_value)==False) :
                # oops! there is no longer time slot available for the day . User must try again the next day
                # : Note we have passed in end_time_value instead of end_time. We need this value to do comparism
                return Utilities.response_formatter(error=True, message=msg_no_slot)
            
            # there is no existing schedule for today, add as new starting from our current timer position
            WorkOrder.objects.create(
                service_id=service_id,
                employee_id=employee_id,
                customer_id=email,
                duration=service_duration,
                description=service_description,
                deleted=0,
                done=0,
                start_time=current_time,
                end_time=end_time,
                end_date =end_date,
                start_time_value=current_time_value,
                end_time_value=end_time_value,
            )
            return Utilities.response_formatter(error=False, message="New work order schedule added")
        else:
            deleted_schedules = scheduled_order_list.filter(
                start_time_value__gte=current_time_value, deleted=1)

            # we will only select deleted schedules where start_time is or beyond the current time since we cannot go back

            if (len(deleted_schedules) > 0):
                # there are valid deleted schedules that can be assigned
                # we wil assign the current schedule to the slot of this deleted schedule since the slot is available
                # pick the necessary details for the deleted schedule and use for this current schedule
                
                deleted_schedule_id = deleted_schedules.values_list(
                    'id', flat=True).first()
                # we will use this value to set the value ``deleted=0`` once slot is successfully reassigned to another customer
                deleted_schedule_start_time = deleted_schedules.values_list(
                    'start_time', flat=True).first()
                deleted_schedule_start_time_value = deleted_schedules.values_list(
                    'start_time_value', flat=True).first()
                deleted_schedule_end_time = deleted_schedules.values_list(
                    'end_time', flat=True).first()
                deleted_schedule_end_date = deleted_schedules.values_list(
                    'end_date', flat=True).first()
                deleted_schedule_end_time_value = deleted_schedules.values_list(
                    'end_time_value', flat=True).first()
                deleted_schedule_duration = deleted_schedules.values_list(
                    'duration', flat=True).first()

                if(float(deleted_schedule_duration) == float(service_duration)):
                    """ We could validate the ``duration`` against the ``deleted_schedule_duration`` 
                    But this should at least be the same. It can only diverge if there is an update to the service duration betwen 
                    when scheduling had already started. 

                    for out implementation to work therefore, both must be the same before we can assign it to deleted schedule
                    any variance means this assignment will make this schedule creeps into another schedule slot, if there is any 

                    :Note: service duration updates must be done at the start of a  new day

                    Assing this new schedule to the first available deleted slot. This will replace the deleted slot with our new schedule
                    """

                    deleted_schedules.filter(id=deleted_schedule_id).update(
                        service_id=service_id,
                        employee_id=employee_id,
                        customer_id=email,
                        duration=service_duration,
                        description=service_description,
                        deleted=0,
                        done=0,
                        start_time=deleted_schedule_start_time,
                        start_time_value=deleted_schedule_start_time_value,
                        end_time=deleted_schedule_end_time,
                        end_date=deleted_schedule_end_date,
                        end_time_value=deleted_schedule_end_time_value,
                    )

                    # deleted_schedules.filter(
                    #     id=deleted_schedule_id).update(deleted=0, done=-1)
                    # # reset the value on the deleted field to be 0 so that we don't pick this again the next time
                    return Utilities.response_formatter(error=False, message="New work order schedule added to existing slot")
                else:
                    # we could do some complex implementation in the fututre. But for now, we will just assume service_duration cannot be changed when scheduling has already started
                    # therefore we will force this schedule to a new slot, but we will report it in the response message
                    return Utilities.response_formatter(error=True, message="Service duration changed during shift. Please service duration update must be done at the start of the day.")
            else:
                """
                There are no deleted slots. So this schedule must be added after the last scheduled entry

                There are few things to consider:

                : 1 - if the ``end_time_value`` of the last schedule slot  is greater than ``start_time_value`` of current  schedule
                    This means that the last schedule runs well into the future beyond our current ``start_time_value"
                    therefore, we will use the ``end_date_value`` of the last schedule item as the  ``start_time_value`` for curent schedule
                    and will recalculate the current schedule ``end_time_value`` using the duration

                : 2 - if not, we will simply use the current values as this current schedule ``start_time_value`` is either equal to the last entry ``end_time_value`` 
                    or greater than it. Anyway, we can safely use the current value
                """
                last_schedule_end_time= scheduled_order_list.values_list('end_time', flat=True).last()
                # textaul representation of the end_time last schedule
                last_schedule_end_time_value= scheduled_order_list.values_list('end_time_value', flat=True).last()
                # number representation of the end_time of last schedule 

                if(float(last_schedule_end_time_value) > float(current_time_value)):
                    # since last schedule still runs into the future, the our start_time and start_time_value will be equiv to the end time values of the last schedule
                    current_time= last_schedule_end_time
                    current_time_value= last_schedule_end_time_value

                    current_end_time_object= datetime.strptime(current_time, '%H:%M:%S')+timedelta(minutes=service_duration)
                    """ Note: service duration is always in minutes"""
                    end_time = current_end_time_object.strftime('%H:%M:%S')

                    end_date = end_time_date_object.strftime('%Y-%m-%d')
                    # the end date is needed for services that spans beyond a day
                    
                    end_time_value = end_time.replace(':', '')

                if(Utilities.is_slot_within_closing_hour(closing_hour=closing_hour, slot_end_time=end_time_value)==False) :
                # validate slot availability
                    return Utilities.response_formatter(error=True, message=msg_no_slot)

                WorkOrder.objects.create(
                    # this insert will handle the two cases above. 
                    service_id=service_id,
                    employee_id=employee_id,
                    customer_id=email,
                    duration=service_duration,
                    description=service_description,
                    deleted=0,
                    done=0,
                    start_time=current_time,
                    start_time_value=current_time_value,
                    end_time=end_time,
                    end_date=end_date,
                    end_time_value=end_time_value,
                )

                return Utilities.response_formatter(error=False, message="Service request successfully added")
    
    def delete_order(request):
        """
        Handles service request order deletion

        """

        id = request.GET.get('id')

        forced = request.GET.get('forced')
        """
        if provided, request will not only be marked as deleted, but will also be removed from the record entry

        : default value is ``0`` whhich is false. Pass value ``1`` to implement ``forced``
        """

        if(id == None):
            """ validate inputs all inputs. All are required """
            return Utilities.response_formatter(True, "id must be provided")

        if(float(forced) == 1):
            delete_result = WorkOrder.objects.filter(id=id).delete()
            # ensure we use all parameters required are provided
            if(delete_result == 0):
                return Utilities.response_formatter(error=True, message="Could not delete. Please check id provided ")
                # result deletion is not successfuls
            return Utilities.response_formatter(error=False, message="Order schedule {} completely deleted ".format(id))
            # deletion was successful

        delete_result = WorkOrder.objects.filter(
            id=id).update(deleted=1, done=-1)
        # here, we have remove the worrk schedule, but we still have it in the database for future reference
        # use done=-1 to indicate that this is a negative order done. Order will not be refernce as a proper done

        if(delete_result == 0):
            return Utilities.response_formatter(error=True, message="Could not delete. Please check id provided ")
            # result deletion is not successful

        return Utilities.response_formatter(error=False, message="Order schedule {}  deleted ".format(id))
        # deletion was successful

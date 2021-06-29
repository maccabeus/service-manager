from _typeshed import IdentityFunction
from api.models import WorkOrder, Service, AppSettings, Holiday
from api.library.utilities import Utilities
from api.serializers import  WorkOrderSerializer, ServiceSerializer
from datetime import datetime, timedelta
import pytz

class WorkOrderManager:
    """
    Expose the necessary API to communicate with the  user scheduled work orders
    """
    formatter = None

    def search_order(request):

        email= request.GET.get('email')
        # the customer's email. 
        service_id=  request.GET.get('service_id')

        if(email==None or service_id==None):
            """
            for each search request, the customer email must be provided
            """
            return Utilities.response_formatter(True, "email and service_id must be provided")

        try:
            orders=WorkOrder.objects.filter(service_id=service_id, customer_email= email)
            """
            search service schedules using only the service_id
            this is the ``service_id`` previously issued to the customer
            """

            if(len(orders) <=0) :
                # if not work order found, return empty data
                return Utilities.response_formatter(False, "No work order found", [])

            serialized_orders= WorkOrderSerializer(orders , many=True)
            # serialize data and return 
            return Utilities.response_formatter(False, "Work order found", serialized_orders.data)

        except:
            return Utilities.response_formatter(True, "Erro occurs. Please try again")
            """ an error occurs and we must retry"""
        
    def search_order_by_date_range(request):
        """
        Search work order using the date range provided. both ``date_from`` and ``date_to``
        must be provided for this to work as we search through the date ranges

        Args:
            request ([object]): [http request object]

        Returns:
            [object]: [http response object]
        """        

        email= request.GET.get('email')
        # the customer's email. 
        date_from=  request.GET.get('date_from')
        date_to= request.GET.get('date_to')

        service_id=  request.GET.get('service_id')
        # if service_id is also provided, we will use as part of our data filter

        if(email==None):
            """
            for each search request, the customer email must be provided
            """
            return Utilities.response_formatter(True, "Email must be provided")

        if(date_from == None or date_to == None):
            """
            validate the date ranhes provided. Both must be available
            """
            return Utilities.response_formatter(True, "date_from and date_to must be provided")

        #try:
        """
        search service schedules using only the email and date range provided
        """
        if(service_id!= None):
            orders=WorkOrder.objects.filter(date_created__range=[date_from, date_to], service_id=service_id)
            # filter also using the ``service_id```

        orders=WorkOrder.objects.filter(date_created__range=[date_from, date_to])
        # select model using only the date_from and date_to

        if(len(orders) <=0) :
            # if not work order found, return empty data
            return Utilities.response_formatter(False, "No work order found for date range", [])

        serialized_orders= WorkOrderSerializer(orders , many=True)
        # serialize data and return 
        return Utilities.response_formatter(False, "Work order found", serialized_orders.data)

        # #except:
        #     return Utilities.response_formatter(True, "Erro occurs. Please try again")
        #     """ an error occurs and we must retry"""

    
    def add_order(request):
        """
        Handles the addition creation of new service request. There are some valid consideration before a service request can be added:

        : The day cannot be ``Sunday``
        : Service request cannot be earlier than 9:00 AM and not later than 5:PM  (Mon- Saturday)
        : Service Request cannot be on an holiday. 

        :Note: we have updated some holidays in the holiday table

        """
        email= request.data.get('email')
        service_id=  request.data.get('service_id')

        user_timezone=  request.data.get('user_timezone')
        # if we provide timezone, this must be same with our orginization timezone 
        # we could also convert other users timezones to our organization's time zone
        
        try:
            """  Get application settings. """
            app_settings=AppSettings.objects.all()

            if(len(app_settings) <=0):
                # app at least one  settings must be defined for app to function
                return Utilities.response_formatter(True, "App settings not defined")
        except:
            return Utilities.response_formatter(True, "Error while loading App Settings")

        opening_hour=app_settings.filter(setting='opening_hour').values_list('value', flat=True).first() or 9
        # schedule cannot be earlier than this opening hour. default to 9:00AM

        closing_hour=app_settings.filter(setting='closing_hour').values_list('value', flat=True).first() or 17
        # schedule cannot be later than the closing hour.  default to 5:00PM 

        app_timezone=app_settings.filter(setting='timezone').values_list('value', flat=True).first() or 'UTC'
        # app timezone will be use while creating time slot for service

        if(email==None):
            """ validate inputs"""
            return Utilities.response_formatter(True, "email must be provided")

        if(service_id==None):
            return Utilities.response_formatter(True, "service_id must be provided")
        
        service_details= Service.objects.filter(id= service_id)
        """ if service details not found, we will stop execution and notify of error"""
        if(len(service_details) <=0):
            return Utilities.response_formatter(True, "Service details not found. Please ensure you have prodived the correct service_id")
        
        current_date=datetime.now()
        # current_date=datetime.now(pytz.)
        """ 
        we will utilize the server date for service request date consistency
        if timezone is provided, this timezone must be consistent with our app timezone

        if user timezone is different from app timezone, we must convert the user time to app timezone 
        equivalent
        """
        current_day= current_date.day
        current_hour= current_date.hour

        if(current_day == 0) :
            # we cannot schedule service request on a sunday
            return Utilities.response_formatter(error=True, message="Cannot schedule service request on Sunday")

        # used for testing current_hour=10
        if(current_hour <  int(opening_hour)) :
            """ for  every other weekdays, validate against the ``opening_hour`` and ``closing_hour`` """
            return Utilities.response_formatter(error=True, message="Cannot schedule earlier than {}:00AM".format(opening_hour))

        if(current_hour >  int(closing_hour)) :
            """ we cannot create service that is already beyond the closing_hour """
            return Utilities.response_formatter(error=True, message="Cannot schedule earlier than {}:00PM.".format(closing_hour)) 
            
        search_date=current_date.strftime('%Y-%m-%d')
        # format the date in to harmonize with our model format
        
        holiday= Holiday.objects.filter(date=search_date)
        # if there is an holiday, we cannot schedule work 
        if(len(holiday) > 0):
            holiday_name= holiday.values_list('description', flat=True).first()
            return "There is {} holiday on {} ".format(holiday_name, search_date)

        """
        Finally, we must attempt to generate service request for this customer
        To generate service request, we will consider the followings:

        : 1.    If there are deleted request on this date, we must use them during the request creation but they must meet the following:
                    " the start_time of such deleted request must be greater

        """

    def delete_order(request):
        """
        Handles service request order deletion

        : 
        """
        email= request.data.get('email')
        service_id=  request.data.get('service_id')
        request_id=  request.data.get('request_id')

        forced_delete=  request.data.get('forced_delete')
        """
        if provided, request will not only be marked as deleted, but will also be removed from the record entry

        : default value is ``0`` whhich is false. Pass value ``1`` to implement ``forced_delete``
        """

        if(email==None):
            """ validate inputs all inputs. All are required"""
            return Utilities.response_formatter(True, "email must be provided")

        if(service_id==None):
            return Utilities.response_formatter(True, "service_id must be provided")

        if(request_id==None):
            return Utilities.response_formatter(True, "request_id must be provided")
        
        if(forced_delete==1):
            WorkOrder.objects.filter(id=request_id, service_id=service_id, customer_email= email).delete()
            # ensure we use all parameters required are provided
            return Utilities.response_formatter(error=False, message="Order schedule {} completely deleted ".format(service_id)) 
        
        WorkOrder.objects.filter(id=request_id, service_id=service_id, customer_email= email).update(deleted=1, done=1)
        # here, we have remove the worrk schedule, but we still have it in the database for future reference
        return Utilities.response_formatter(error=False, message="Order schedule {}  deleted ".format(service_id)) 

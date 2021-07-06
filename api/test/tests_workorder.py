from datetime import date, datetime
from django.test import TestCase, RequestFactory
from api.models import WorkOrder, Holiday, AppSettings, Service
from api.api_views import workorder_add, workorder_delete, workorder_search, workorder_search_by_date_range


class WorkOrderTest(TestCase):

    def setUp(self):

        self.factory= RequestFactory()

        self.service_duration = 120
        # service duration is 120 nminutes

        self.employee_id=1
        self.customer_id=10
        self.description = "Sample Test Service"

        """
        Create some data entry for test purposes
        """
        self.service= Service.objects.create(
            name="Test Service",
            duration=self.service_duration,
            description=self.description,
        )
        self.service.save()
        self.service_id = self.service.pk
        
        self.test_email = "test@gmail.com"

        self.start_time = "08:00:00"
        self.start_time_value = 80000
        self.end_time = "12:00:00"
        self.end_time_value = 120000

        """
        Some invalid variables
        """
        self.holiday_date_str="2021-07-01"

        self.mock_holiday_date="2021-07-01T13:00:00.000000"
        # simulate holiday date but valid time

        self.mock_valid_date_time="2021-09-01T13:00:00.000000"
        # simulate a valid time and date


        self.mock_late_time="2021-08-01T18:00:00.000000"
        # simulate a valid time and date

        """
        some variable for our calls
        """
        self.add_order_data={'email': self.test_email, 'service_id': self.service_id, 'current_date_mock': self.mock_valid_date_time}

        self.mock_order_data_invalid_date={'email': self.test_email, 'service_id': self.service_id, 'current_date_mock': self.mock_holiday_date}
        # mocks invalid date for holidy testing
        
        order_request=WorkOrder.objects.create( 
            service_id=self.service_id,
            employee_id=self.employee_id,
            customer_id=self.customer_id,
            duration=self.service_duration,
            description=self.description,
            deleted=0,
            done=0,
            start_time=self.start_time,
            start_time_value=self.start_time_value,
            end_time=self.end_time,
            end_time_value=self.end_time_value,
        )
        order_request.save()

        self.order_reequest_id= order_request.pk
        # this is the created order request ID. we will use while deleting order request

        Holiday.objects.create( 
            # create a test holiday
           date=self.holiday_date_str,
           description="Test Holiday"
        )

        # create app settings
        AppSettings.objects.create(setting="opening_hour", value=9)
        AppSettings.objects.create(setting="closing_hour", value=17)
        AppSettings.objects.create(setting="timezone", value='UTC')


    def test_add_order(self) : 
        """ 
        Test the addition of a new work order schedule 
        """

        request= self.factory.post('/workorder', self.add_order_data)

        response=workorder_add(request)

        self.assertEqual(response.status_code, 200, "Must make a valid post to workorder")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")
        self.assertIn('data', response.data, "Must have data key")

        self.assertEqual(response.data['error'], False, "Must add a new work order schedule")
    

    def test_add_order_not_on_holiday(self) : 
        """ 
        Addition of new service request must not fall on an holiday
        """

        request= self.factory.post('/workorder', self.mock_order_data_invalid_date)

        response=workorder_add(request)

        self.assertEqual(response.status_code, 200, "Must make a valid post to workorder")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")
        self.assertIn('data', response.data, "Must have data key")

        self.assertEqual(response.data['error'], True, "Must not add order schedule on an holiday")
        
    def test_add_order_early_request(self) : 
        """ 
        Addition of new service request must not be earlier than the opening hour
        """
        mock_call_data={'email': self.test_email, 'service_id': self.service_id, 'current_date_mock': '2021-08-01T07:00:00.000000'}
        # mock time earlier than the opening hour

        request= self.factory.post('/workorder', mock_call_data)

        response=workorder_add(request)

        self.assertEqual(response.status_code, 200, "Must make a valid post to workorder")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")
        self.assertIn('data', response.data, "Must have data key")
        

        self.assertEqual(response.data['error'], True, response.data['message'])


    def test_add_order_late_request(self) : 
        """ 
        Addition of new service request must not be later than the closing hour
        """
        mock_call_data={'email': self.test_email, 'service_id': self.service_id, 'current_date_mock': '2021-08-01T18:00:00.000000'}

        request= self.factory.post('/workorder', mock_call_data)

        response=workorder_add(request)

        self.assertEqual(response.status_code, 200, "Must make a valid post to workorder")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")
        self.assertIn('data', response.data, "Must have data key")

        self.assertEqual(response.data['error'], True, response.data['message'])

    def test_add_order_sunday_request(self) : 
        """ 
        Addition of new service request cannot be on Sunday
        """
        mock_call_data={'email': self.test_email, 'service_id': self.service_id, 'current_date_mock': '2021-06-27T13:00:00.000000'}
        # mock a valid time and a date that falls on Sunday

        request= self.factory.post('/workorder', mock_call_data)

        response=workorder_add(request)

        self.assertEqual(response.status_code, 200, "Must make a valid post to workorder")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")
        self.assertIn('data', response.data, "Must have data key")

        self.assertEqual(response.data['error'], True, response.data['message'])

    def test_add_delete(self) : 
        """ 
        Deletes a scheduled  work order request
        """

        mock_call_data={'id': self.order_reequest_id}

        print(mock_call_data, "mock data")

        request= self.factory.post('/workorder/delete', mock_call_data)

        response=workorder_add(request)

        self.assertEqual(response.status_code, 200, "Must make a valid delete call to workorder/delete")

        print(response.data, "response data")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")

        self.assertEqual(response.data['error'], False, "Order delete error status must be False")

        self.assertContains(response.data['message'], 'Could not delete', "Order must be deleted successfully")

    
    def tearDown(self) -> None:
        # clean up after all test cases
        return super().tearDown()
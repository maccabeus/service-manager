from django.test import TestCase, RequestFactory
from api.models import Service
from api.api_views import service, service_by_id

class ServiceTest(TestCase):

    def setUp(self):
        self.factory =  RequestFactory()

        """
        Add test Data 
        """
        Service.objects.create(name="iPhone Screen Repairs", description="Amazing iPhone repair services", duration=120)

    
    def test_service (self):

        request= self.factory.get('/service')
        
        response=service(request)

        self.assertEqual(response.status_code, 200, "Must make a valid get call to service")

        self.assertIn('error', response.data, "Must have error key")
        self.assertIn('message', response.data, "Must have message key")
        self.assertIn('data', response.data, "Must have data key")

        self.assertGreater(len(response.data['data']), 0, "Must return at least 1 service list" )

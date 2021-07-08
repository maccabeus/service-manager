
from api.models import Service
from api.library.utilities import Utilities
from api.serializers import ServiceSerializer

class ServicesManager : 
    """
    Handles all service call for our service manager API.

    Exposes all the methods we need to communicate with our application services
    """
    def service(self):
        """
        return all available services application offers
        """
        # try:
        services= Service.objects.filter(pk__gt=0)
        service_serializer= ServiceSerializer(services , many=True)
        return Utilities.response_formatter(False, "Record Found", service_serializer.data)
        # except:
        #     return Utilities.response_formatter(True, "Error occurs. Please try again")

    def service_by_id(request, service_id):
            """
            return the detail of a service with the provided ``service_id``
            """
            try:
                services= Service.objects.filter(id=service_id)
                service_serializer= ServiceSerializer(services , many=True)
                return Utilities.response_formatter(False, "Record Found", service_serializer.data)
            except:
                return Utilities.response_formatter(True, "Error occurs. Please try again")
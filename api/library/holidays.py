
from api.models import Holiday
from api.library.utilities import Utilities
from api.serializers import HolidaySerializer

class HolidayManager : 
  
    def get_all(self):
        """
        return all available services application offers
        """
        try:
            holidays= Holiday.objects.all()
            holiday_serializer= HolidaySerializer(holidays , many=True)
            return Utilities.response_formatter(False, "Record Found", holiday_serializer.data)
        except:
            return Utilities.response_formatter(True, "Error occurs. Please try again")

    def service_by_id(request, holiday_id):
            """
            return the detail of a service with the provided ``service_id``
            """
            try:
                holidays= Holiday.objects.filter(pk=holiday_id)
                holiday_serializer= HolidaySerializer(holidays , many=True)
                return Utilities.response_formatter(False, "Record Found", holiday_serializer.data)
            except:
                return Utilities.response_formatter(True, "Error occurs. Please try again")
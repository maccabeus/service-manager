
from api.models import Employee
from api.library.utilities import Utilities
from api.serializers import EmployeeSerializer

class EmployeeManager : 
  
    def get_all(self):
        """
        Get the avialable employee records
        """
        try:
            employees= Employee.objects.all()
            employee_serializer= EmployeeSerializer(employees , many=True)
            return Utilities.response_formatter(False, "Employee Record Found", employee_serializer.data)
        except:
            return Utilities.response_formatter(True, "Error occurs. Please try again")

    def get_by_id(request, holiday_id):
            """
            Get the employee with the ``employee_id``
            """
            try:
                employees= Employee.objects.filter(pk=holiday_id)
                employee_serializer= EmployeeSerializer(employees , many=True)
                return Utilities.response_formatter(False, "Employee Record Found", employee_serializer.data)
            except:
                return Utilities.response_formatter(True, "Error occurs. Please try again")
    
    def get_available_employee_id():
            """
            Get  any available free employee that can be assign to a work order
            """
            return 2

    
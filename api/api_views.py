from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from api.library.services import ServicesManager
from api.library.customer import CustomerManager
from api.library.employee import EmployeeManager
from api.library.holidays import HolidayManager
from api.library.workorder import WorkOrderManager

# ---------------------------------------------------------------------------------
# ----------------------------------- Service Routes -----------------------------
# ---------------------------------------------------------------------------------

@api_view(['GET'])
def service(request):
    """
    Return the list of available services 
    Returns:
        [json]: [returns a jason string]
    """
    service_manager = ServicesManager
    return Response(service_manager.service(request))


@api_view(['GET'])
def service_by_id(request, service_id: int):
    """[Get service by ID]

    Args:
        service_id (int): [the id of the service. ``pk``]

    Returns:
        [type]: [http response object]
    """
    service_manager = ServicesManager
    return Response(service_manager.service_by_id(request, service_id))

# ---------------------------------------------------------------------------------
# ----------------------------------- Customer Routes -----------------------------
# ---------------------------------------------------------------------------------

@api_view(['GET'])
def customer(request: Request):
    """Return the list of available customers

    Returns:
        [json]: [returns a jason string]
    """
    customer_manager = CustomerManager
    return Response(customer_manager.get_all(request))


@api_view(['GET'])
def customer_get_by_email(request: Request, email: str):
    """Get a customer details  by email

    Args:
        email (str): [customer's email address]

    Returns:
        [json]: [returns a jason string]
    """
    customer_manager = CustomerManager
    return Response(customer_manager.getByEmail(request, email))

# ----------------------------------------------------------------------------------
# ----------------------------------- Holiday Routes -------------------------------
# ----------------------------------------------------------------------------------

@api_view(['GET'])
def holiday(request: Request):
    """Get the list of available holiday

    Returns:
        [json]: [returns a jason string]
    """
    holiday_manager = HolidayManager
    return Response(holiday_manager.get_all(request))


@api_view(['GET'])
def holiday_by_id(request, holiday_id: int):
    """[Get holiday using the provided ``holiday_id``]

    Args:
        holiday_id (int): [the  id of the holiday provided]

    Returns:
        [type]: [http response object]
    """
    holiday_manager = HolidayManager
    return Response(holiday_manager.service_by_id(request, holiday_id))

# ----------------------------------------------------------------------------------
# ----------------------------------- Employee Routes ------------------------------
# ----------------------------------------------------------------------------------

@api_view(['GET'])
def employee(request: Request):
    """Get list of employees

    Returns:
        [json]: [returns a jason string]
    """
    employee_manager = EmployeeManager
    return Response(employee_manager.get_all(request))


@api_view(['GET'])
def employee_by_id(request, employee_id: int):
    """[Returns the employee with the provided  ``employee_id``]

    Args:
        employee_id (int): [the  id of the holiday provided]

    Returns:
        [type]: [http response object]
    """
    employee_manager = EmployeeManager
    return Response(employee_manager.get_by_id(request, employee_id))

# ----------------------------------------------------------------------------------
# ----------------------------------- Work Order Routes ----------------------------
# ----------------------------------------------------------------------------------

@api_view(['POST'])
def workorder_add(request):
    """Add a new work order 

    Args:
         email (str): [customers email address ]
         service_id (int): [Service id to schedule]

    Returns:
        [json]: [returns a jason string]
    """
    order_manager = WorkOrderManager
    return Response(order_manager.add_order(request))

@api_view(['GET'])
def workorder_search(request: Request):
    """
    Search the list work orders and find an order either 
    By ``id`` or by the provided ``email``

    Args:
            email (str): [customers email address ]
            service_id (int): [optiona - service id  ]

    Returns:
        [json]: [returns a jason string]
    """
    order_manager = WorkOrderManager
    return Response(order_manager.search_order(request))

@api_view(['GET'])
def workorder_search_by_date_range(request: Request):
    """
    Search the list of work orders by the provided ``date range``

    Args:
        email (str): [customers email address ]
        date_from (str): [start date range ]
        date_to (str): [end date range ]
        service_id (int): [optiona - service id  ]

    Returns:
        [json]: [returns a jason string]
    """
    order_manager = WorkOrderManager
    return Response(order_manager.search_order_by_date_range(request))

@api_view(['DELETE'])
def workorder_delete(request):
    """
    Delete a work order service request

    Args:
         id (int): [the request ID  ]
         forced (int): [optional - will delete completely from system. Must be use for admin purposes. Slot cannot be reassigned if this param is used ]

    Returns:
        [json]: [returns a jason string]
    """
    order_manager = WorkOrderManager
    return Response(order_manager.delete_order(request))
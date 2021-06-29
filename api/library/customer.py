from api.models import Customer
from api.serializers import CustomerSerializer

class CustomerManager: 
    """
    Manages customers interations with API
    """
    def get_all(self):
        customers= Customer.objects.all()
        customers_serializer= CustomerSerializer(customers, many=True)
        return ({'error': False, 'message': 'Record found', 'data': customers_serializer.data})

    def getByEmail(request, email=None) :
        """
        Get customer details using the customers email address
        """
        if(email==None):
            # we cannot process withhout a valid email
            return ({'error': True, 'message': 'Id must be provided', 'data': []})
        try:
            customer= Customer.objects.filter(email= email)
            if(len(customer)< 1):
                return ({'error': False, 'message': 'Record found', 'data': []})
                # no record was found matching this criteria

            customer_serializer= CustomerSerializer(customer , many=True)
            # serialize and return customer record
            return ({'error': False, 'message': 'Record found', 'data': customer_serializer.data})
        except:
            # there is an error and notthing found
            return ({'error': True, 'message': 'Error occur while getting details', 'data': []})
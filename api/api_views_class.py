from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from api.models import Customer
from api.serializers import CustomerSerializer

class GetCustomers(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class GetCustomerByEmail(generics.ListAPIView):
    """
    """
    email=None

    queryset = customer= Customer.objects.get(email=kwargs['email'])
    serializer_class = CustomerSerializer
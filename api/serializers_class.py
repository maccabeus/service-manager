from rest_framework import serializers
from api.models import Customer, Employee, Service,WorkOrder, Holiday

"""
Handles all API serializations. All response returned in JSON fomat
"""
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['name', 'email', 'phone','date_created', 'time_created', 'updated_at']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Service
        fields=['name', 'description', 'duration','date_created', 'time_created', 'updated_at']

class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=WorkOrder
        fields=['service_id','customer_id ','employee_id', 'description', 'duration ','date_created', 'time_created', 'updated_at']

class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model=Employee
        fields=['name', 'email', 'phone','department','date_created', 'time_created', 'updated_at']

class HolidaySerializer(serializers.Serializer):
    class Meta:
        model=Holiday
        fields=['description','date']
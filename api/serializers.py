from rest_framework import serializers

"""
Handles all API serializations. All response returned in JSON fomat
"""
class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.FloatField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class WorkOrderSerializer(serializers.Serializer):
    service_id =  serializers.IntegerField()
    customer_id =  serializers.IntegerField()
    employee_id = serializers.IntegerField()
    description = serializers.CharField()
    duration = serializers.FloatField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    department =serializers.CharField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class HolidaySerializer(serializers.Serializer):
    description = serializers.CharField()
    date = serializers.DateField()
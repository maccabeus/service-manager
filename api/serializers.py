from rest_framework import serializers

"""
Handles all API serializations. All response returned in JSON fomat
"""
class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.FloatField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class WorkOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    service_id =  serializers.IntegerField()
    customer_id =  serializers.EmailField()
    employee_id = serializers.IntegerField()
    description = serializers.CharField()
    duration = serializers.FloatField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()
    
    start_time = serializers.CharField()
    end_time = serializers.CharField()
    start_time_value = serializers.FloatField()
    end_time_value = serializers.FloatField()
    end_date = serializers.CharField()

class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    department =serializers.CharField()
    date_created = serializers.DateField()
    time_created = serializers.TimeField()
    updated_at =serializers.DateTimeField()

class HolidaySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField()
    date = serializers.DateField()
from django.db import models

class Customer (models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_created', ]),
            models.Index(fields=['id', ])
        ]

    """ The application customer"""
    name = models.CharField(max_length=250, help_text="The customer's name")
    email = models.EmailField(
        max_length=100, help_text="user valid email address")
    phone = models.CharField(
        max_length=100, help_text="user valid phone number")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="date customer's account was created")
    time_created = models.TimeField(
        auto_now_add=True, verbose_name="time customer's account was created")
    updated_at = models.DateTimeField(
        null=True, verbose_name="date customer's account was created", auto_now=True)

class Employee(models.Model):
    """ The list of staffs and their details"""

    class Meta:
        indexes = [models.Index(fields=['id'])]

    name = models.CharField(max_length=250, help_text="The staff's name")
    email = models.EmailField(
        max_length=100, help_text="staff valid email address")
    phone = models.CharField(
        max_length=100, help_text="staff valid phone number")
    department = models.CharField(
        max_length=100, help_text="departmen of the staff")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="date staff's account was created")
    time_created = models.TimeField(
        auto_now_add=True, verbose_name="time staff's account was created")
    updated_at = models.DateTimeField(
        null=True, verbose_name="date staff's account was created", auto_now=True)

class Holiday (models.Model):
    """ the available holidays when services is not available"""

    class Meta:
        indexes=[models.Index(fields=['date'])]

    date = models.DateField(
        auto_now_add=True, verbose_name=" holiday date when services cannot be booked")
    description = models.TextField(
        help_text="Brief description about this holiday")


class Service (models.Model):
    """ Types of services available for clients to choose from"""

    class Meta:
        indexes = [
            models.Index(fields=['date_created', ]),
            models.Index(fields=['id', ])
        ]

    name = models.CharField(
        max_length=100, help_text="The name of this service")
    description = models.CharField(
        max_length=100, help_text="The service description. What this service is all about")
    duration = models.FloatField(
        verbose_name="The duration in minues required for task completion")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="date service is created")
    time_created = models.TimeField(
        auto_now_add=True, verbose_name="time service is created")
    updated_at = models.DateTimeField(
        null=True, verbose_name="date and time service is updated")


class WorkOrder(models.Model):

    """ 
    The schedule list of orders made by customers"
    create indexes using the ``date_created`` and the ``id`` fields for our search
    """
    class Meta:
        indexes = [
            models.Index(fields=['date_created']),
            models.Index(fields=['customer_email']),
            models.Index(fields=['deleted']),
            models.Index(fields=['done']),
            models.Index(fields=['id']),
            models.Index(fields=['start_time']),
            models.Index(fields=['end_time']),
        ]

    service_id = models.BigIntegerField(
        verbose_name="the service Id linked to this order")
    customer_id = models.BigIntegerField(
        verbose_name="the customer Id linked to this order")
    employee_id = models.BigIntegerField(
        verbose_name="the emplyee Id assigned to treat this order")
    description = models.TextField(help_text="The order descriptions")
    customer_email = models.EmailField(
        max_length=100, help_text="The customer's email address", default="")
    duration = models.FloatField(
        verbose_name="The duration in minues required for task completion")
    date_created = models.DateField(
        auto_now_add=True, verbose_name="date order is created")
    time_created = models.TimeField(
        auto_now_add=True, verbose_name="time order is created")
    start_time = models.TimeField(verbose_name="The actual time the order is scheduled to start", default= None)
    end_time = models.TimeField(verbose_name="The time the order is scheduled to end", default= None)
    updated_at = models.DateTimeField(
        null=True, verbose_name="date and time order is updated")
    done = models.BigIntegerField(
        verbose_name="Will be 1 when service request is done", default=0)
    deleted = models.BigIntegerField(
        verbose_name="A field to track deleted request> this request will be available for audit purposes", default=0)

class AppSettings(models.Model):
    """ This is the application settings model"""

    class Meta:
        indexes = [models.Index(fields=['id'])]
        indexes = [models.Index(fields=['value'])]
        indexes = [models.Index(fields=['setting'])]

    setting = models.CharField(max_length=250, help_text="Setting name")
    value = models.CharField(max_length=250, help_text="value of the setting")

from django.contrib import admin
from django.urls import path
from rest_framework.decorators import api_view
from api import views, api_views

urlpatterns = [

    path('', views.index),
    # Show the api index page. This could contain the docs

    path('service', api_views.service),
    # get all services
    path('service/<int:service_id>', api_views.service_by_id),
    # get service by id ``pk``

    path('holidays', api_views.service),
    # get all available holidays
    path('service/<int:holiday_id>', api_views.service_by_id),
    # get holday with th provided ``holoday_id```

    path('customer', api_views.customer),
    # get customers list
    path('customer/<str:email>', api_views.customer_get_by_email),
    # use email adress to get customer's details

    path('holiday', api_views.holiday),
    # get the available holidays
    path('holiday/<int:holiday_id>', api_views.holiday_by_id),
    # get the holiday with the provided ``holiday_id``

    path('employee', api_views.employee),
    path('employee/<int:employee_id>', api_views.employee_by_id),

    path('workorder', api_views.workorder_add),
    # Add a new work order
    path('workorder/search', api_views.workorder_search),
    # search the workorder using either ``id``
    path('workorder/search/date', api_views.workorder_search_by_date_range),
    # search the workorder using  ``date range``
    path('workorder/delete', api_views.workorder_delete),
    # search the workorder using  ``date range``
    
]
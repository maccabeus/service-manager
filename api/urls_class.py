
from django.contrib import admin
from django.urls import path, include
from api import views, api_views_class
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index),
    # Show the api index page. This could contain the docs

    # path('service', api_views.service),
    # # all services related routes goes here

    path('customers', api_views_class.GetCustomers.as_view()),
    # all customer related routes are added here

    path('customer/<str:email>', api_views_class.GetCustomerByEmail.as_view()),
    # get customers details by using the provided email address
]

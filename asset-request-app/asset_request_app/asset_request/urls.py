from django.contrib import admin
from django.urls import path
from .views import laptop_request, redirect_request

urlpatterns = [
    path('laptop-request', laptop_request, name='laptop-request'),
    path('', redirect_request)
]

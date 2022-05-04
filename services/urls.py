from django.urls import path
from . import views

urlpatterns=[
    path('service',views.service_request, name='service'),
    path('servicedetails', views.single_request, name='servicedetails'),
]
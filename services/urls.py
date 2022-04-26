from django.urls import path
from . import views

urlpatterns=[
    path('services',views.service_request, name='services'),
    path('singleservices', views.single_request, name='singleservices'),
]
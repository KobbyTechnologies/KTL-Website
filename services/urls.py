from django.urls import path
from . import views

urlpatterns=[
    path('services',views.service_request, name='services'),
    path('single', views.single_request, name='single')
]
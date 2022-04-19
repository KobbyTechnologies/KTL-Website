from django.urls import path
from . import views

urlpatterns=[
    path('service',views.service_request, name='service'),
    path('single', views.single_request, name='single')
]
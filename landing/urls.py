from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='index'),
    path('test', views.contact, name='test'),
]


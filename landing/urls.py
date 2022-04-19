from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='index'),
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),

]

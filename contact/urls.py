from django.urls import path
from . import views


urlpatterns = [
    path('contacts', views.contact_view, name='contacts'),
    path('contacts-form', views.contacts_form_view, name='contacts-form'),
]


from django.urls import path
from . import views

urlpatterns=[
    path('Blog',views.Blog_request, name='Blog'),
    path('Blogdetails',views.BLOG2_request, name='Blogdetails'),
]
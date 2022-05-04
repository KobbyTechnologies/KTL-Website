from django.urls import path
from . import views

urlpatterns=[
    path('Blogdetails',views.Blog_request, name='Blogdetails'),
    path('Blog',views.BLOG2_request, name='Blog'),
]
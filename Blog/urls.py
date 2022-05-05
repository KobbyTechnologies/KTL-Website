from django.urls import path
from . import views

urlpatterns=[
    path('blog',views.blog_request, name='blog'),
    path('blog-details',views.blog_detail_request, name='singleblog'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='index'),
    path('solution/', views.solution, name='solution'),
    path('solution-single/', views.solution_view, name='solution_single'),
]

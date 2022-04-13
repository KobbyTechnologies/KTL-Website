from django.urls import path
from . import views


urlpatterns = [
    path('solution/', views.solution, name='solution'),
    path('solution-single/', views.solution_view, name='solution_single'),
]

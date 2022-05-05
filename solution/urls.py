from django.urls import path
from . import views


urlpatterns = [
    path('solution', views.solution, name='solution'),
    path('single-solution', views.solution_view, name='singleSolution'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('library/', views.stories_view, name='library'),
]

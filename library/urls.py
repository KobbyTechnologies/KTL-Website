from django.urls import path
from . import views


urlpatterns = [
    path('success_stories', views.stories_view, name='success-stories'),
    path('story', views.story_detail, name='read_more'),
    path('events', views.events, name='events'),
    path('csr', views.csr_view, name='csr'),
    path('csr-detail', views.csr_detail_view, name='csr-detail'),
    path('gallery', views.gallery_view, name='gallery'),
]

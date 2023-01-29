from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('', include('solution.urls')),
    path('', include('library.urls')),
    path("", include('about.urls')),
    path('', include('services.urls')),
    path('', include('Blog.urls')),
    path('', include('contact.urls')),
]

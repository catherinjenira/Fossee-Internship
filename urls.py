from django.contrib import admin
from django.urls import path, include
from .views import index, favicon

urlpatterns = [
    path('', index),
    path('favicon.ico', favicon),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

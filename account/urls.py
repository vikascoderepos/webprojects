from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    #path('api/users/<user_id>/profile/', ProfileAPI.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
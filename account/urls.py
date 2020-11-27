from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap





urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path("account/<int:pk>/", views.profile_detail, name="profile_detail"),
    path("contact/", views.contact_view, name="contact_view"),
    path("about/", views.about_view, name="about_view"),
    #path('api/users/<user_id>/profile/', ProfileAPI.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



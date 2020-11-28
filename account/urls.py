from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap





urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path("account/<int:pk>/", views.profile_detail, name="profile_detail"),
    path("contact/", views.contact_view, name="contact_view"),
    path("about/", views.about_view, name="about_view"),
    path('api/profiles/',
         views.ProfileListView.as_view(),
         name='profile_api_list'),
    path('api/profile/<pk>/',
         views.ProfileDetailView.as_view(),
         name='profile_api_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



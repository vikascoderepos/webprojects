from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap 
from account.models import Profile 
from django.contrib.sitemaps.views import sitemap

from account.sitemaps import Static_Sitemap
from account.sitemaps import Profile_Sitemap


info_dict = {
    'queryset': Profile.objects.all(),
}

sitemaps = {
    'profile': Profile_Sitemap(),
    'static': Static_Sitemap(),
}


urlpatterns = [
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('account.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from account.models import Profile 


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['about_view', 'contact_view']

    def location(self, item):
        return reverse(item)


class Profile_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Profile.objects.all()

    def lastmod(self, obj): 
        return obj.created_date
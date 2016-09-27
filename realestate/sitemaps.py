from django.contrib.sitemaps import Sitemap
from realestate.models import Main, City


class StateSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return Main.objects.filter(
            available=True).order_by('state').distinct('state')

    def location(self, obj):
        return '/' + str(obj.state) + '/'


class CitySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return City.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

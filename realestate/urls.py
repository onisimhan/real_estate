from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap, index
from rest_framework import routers
from realestate import views
from realestate.sitemaps import StateSitemap, CitySitemap
from django.views.generic import TemplateView
from realestate import feeds
from rest_framework.authtoken import views as authViews

sitemaps = {'cities': CitySitemap, 'states': StateSitemap}

router = routers.DefaultRouter()
router.register(r'main', views.MainViewSet)
router.register(r'removed', views.MainRemovedViewSet)
router.register(r'advanced', views.MainAdvancedViewSet, authViews.obtain_auth_token)

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^googledc6ee21d00cd442a\.html$', views.googledc6ee21d00cd442a.as_view(), name='google site verification'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^request_viewing/', views.MainContact.as_view(), name='contact'),
    url(r'^states/$', views.StateListView.as_view(), name='states'),
    url(r'^contact/$', views.ContactUsView.as_view(), name='contact_us'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^terms/$', views.TermsView.as_view(), name='terms'),
    url(r'^privacy/$', views.PrivacyView.as_view(), name='privacy'),
    url(r'^(?P<s>\w{2})/(?P<c>\w*(-\w*)*?)/$',
        views.PropertyListView.as_view(), name='property_list'),
    url(r'^(?P<s>\w{2})/$',
        views.CityListView.as_view(), name='city_list'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    # Receives as parameters State / City / Address and redirects
    url(r'^(?P<s>\w{2})/(?P<c>\w*(-\w*)*?)/(?P<a>[-\w]*)/$',
        views.old_property_view, name='old_property'),
    # Receives as parameters State / City / Address / ID BUT uses only ID
    url(r'^(?P<s>\w{2})/(?P<c>\w*(-\w*)*?)/(?P<a>[-\w]*)/(?P<pk>\d*)$',
        views.PropertyView.as_view(), name='property'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')),


    # SITEMAPS
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),

    # FEEDS
    url(r'^rss/(?P<s>\w{2})/(?P<c>\w*(-\w*)*?)/$',
        feeds.PropertyFeed(), name='property_feed'),
    # url(r'^rss/(?P<s>\w{2})/$',
    #     feeds.CityFeed(), name='city_feed'),
)

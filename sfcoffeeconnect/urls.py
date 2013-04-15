from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^core/', include('core.urls')),
    # Examples:
    # url(r'^$', 'sfcoffeeconnect.views.home', name='home'),
    # url(r'^sfcoffeeconnect/', include('sfcoffeeconnect.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

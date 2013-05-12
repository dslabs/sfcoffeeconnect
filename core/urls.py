
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.home'),
    url(r'^profile/', 'core.views.profile'),
    url(r'', include('social_auth.urls')),
    # Examples:
    # url(r'^$', 'sfcoffeeconnect.views.home', name='home'),
    # url(r'^sfcoffeeconnect/', include('sfcoffeeconnect.foo.urls')),
)

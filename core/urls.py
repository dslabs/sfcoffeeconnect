from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    # Examples:
    # url(r'^$', 'sfcoffeeconnect.views.home', name='home'),
    # url(r'^sfcoffeeconnect/', include('sfcoffeeconnect.foo.urls')),
)

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from best_bet_predictor.views import *
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'race_analyzer.views.home', name='home'),
    # url(r'^race_analyzer/', include('race_analyzer.foo.urls')),
    (r'^$', home),
    (r'^home/$', home),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

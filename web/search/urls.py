from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('search.views',
    url(r'^search/$', 'search', name='search'),
    url(r'^search/map/$', 'search', name='search_map', kwargs={'search_map': True}),
)

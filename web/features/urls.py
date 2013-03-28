from django.conf.urls.defaults import patterns, url
from feeds import FeaturesFeed

urlpatterns = patterns('features.views',
    url(r'^$', 'news_home', name="news_home"),
    url(r'^features/$', 'feature_list', name="feature_list"),
    url(r'^media/$', 'media_list', name="media_list"),
    url(r'^feed/$', FeaturesFeed(), name="feature_feed"),
    url(r'^features/(?P<slug>[-\w]+)/$', 'feature_detail', name="feature_detail"),
)

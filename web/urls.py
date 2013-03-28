from django.conf.urls.defaults import patterns, include
from web import settings

# Uncomment the next two lines to enable the adminn:
# from django.contrib import admin

from django.contrib.gis import admin
admin.autodiscover()

handler500 = 'frontend.views.server_error'

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', include('data.urls')),
    (r'^news/', include('features.urls')),
    (r'', include('frontend.urls', namespace="my_account")),
    (r'', include('search.urls')),
    (r'', include('countryinfo.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),

    (r'lists/', include('listmaker.urls')),
    (r'^accounts/', include('registration.urls')),

    (r'^api/', include('web.api.urls')),

    (r'^petition/', include('web.petition.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )

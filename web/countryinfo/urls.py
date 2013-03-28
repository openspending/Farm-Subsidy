from django.conf.urls.defaults import url, patterns
import views


urlpatterns = patterns('',
    url(r'^stats/compare',views.compare),
    url(r'^transparency/',views.transparency_list, name="transparency_index"),
)
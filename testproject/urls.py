from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp.views import *
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^product/(?P<id>\d+)/$', full_info),
    #url(r'^ajax/loadcounter/$', load_Counter),
   # url(r'^ajax/playcounter/$', play_Counter),
    
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True}),
)

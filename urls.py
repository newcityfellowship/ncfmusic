from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/',    include('grappelli.urls')),
    (r'^admin/doc/',    include('django.contrib.admindocs.urls')),
    (r'^admin/',        include(admin.site.urls)),
)

if settings.DEBUG:
  urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
  )

urlpatterns += patterns('ncfmusic.apps.content.views',
    (r'^about/$',                                   'about'),
    (r'^listen/$',                                  'listen'),
    (r'^watch/$',                                   'watch'),
    (r'^watch/(?P<slug>[\w-]+)/$',                  'watch'),
    (r'^learn/$',                                   'tutorials'),
    (r'^learn/(?P<slug>[\w-]+)/$',                  'tutorial'),
    (r'^talks/$',                                   'talks'),
    (r'^articles/$',                                'articles'),
    (r'^articles/(?P<slug>[\w-]+)/$',               'article'),
    (r'^songs/$',                                   'songs'),
    (r'^songs/(?P<start_letter>\w{1})/$',           'songs'),
    (r'^events/$',                                  'events'),
    (r'^events/(?P<month>\d{2})/(?P<year>\d{4})/$', 'events'),
    (r'^events/(?P<slug>[\w-]+)/$',                 'event'),
    (r'^churches/$',                                'churches'),
    (r'^churches/(?P<slug>[\w-]+)/$',               'church'),
    (r'^musicians/$',                               'musicians'),
    (r'^musicians/(?P<slug>[\w-]+)/$',              'musicians'),
    (r'^search/$',                                  'search'),
    (r'^$',                                         'home'),
)


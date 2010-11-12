from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/',    include('apps.grappelli.urls')),
    (r'^admin/doc/',    include('django.contrib.admindocs.urls')),
    (r'^admin/',        include(admin.site.urls)),
)

urlpatterns += patterns('ncfmusic.apps.content.views',
    (r'^about/$',                           'about'),
    (r'^listen/$',                          'listen'),
    (r'^watch/$',                           'watch'),
    (r'^tutorials/$',                       'tutorials'),
    (r'^tutorial/(?P<slug>[\w-]+)/$',       'tutorial'),
    (r'^talks/$',                           'talks'),
    (r'^articles/$',                        'articles'),
    (r'^article/(?P<slug>[\w-]+)/$',        'article'),
    (r'^songs/$'                            'songs'),
    (r'^songs/(?P<start_letter>[\w]{1})/$', 'songs'),
    (r'^$',                                 'home'),
)

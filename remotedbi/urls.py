from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'dbmap.views.index', name='home'),
                       url(r'^tables/', 'dbmap.views.view_tables', name='tables'),
                       url(r'^dbadd/', 'dbmap.views.add_db', name='adddb'),
                       url(r'^fields/', 'dbmap.views.view_fields', name='fields'),
                       url(r'^records/', 'dbmap.views.view_records', name='records'),
    # Examples:
    # url(r'^$', 'remotedbi.views.home', name='home'),
    # url(r'^remotedbi/', include('remotedbi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

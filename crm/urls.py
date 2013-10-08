from django.conf.urls import patterns, include, url
from hycrm.views import main_view
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from django.contrib.auth.views import login, logout
from hycrm.views import index,denglu,main_view
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    ('^$', index),
    (r'^crm/$', main_view),
    (r'^crm/main/$', denglu),
)

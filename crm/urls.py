from django.conf.urls import patterns, include, url
from hycrm.views import login_view
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from django.contrib.auth.views import login, logout
from hycrm.views import index,login_view
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^crm/', include('crm.foo.urls')),
    ('^$', index),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', login_view),
    # (r'^accounts/logout/$', logout_view),
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.views import login, logout
from hycrm.views import index
from hycrm.views import main_view
from hycrm.views import main_page
from hycrm.views import main_customer, new_customer, edit_customer
from hycrm.views import main_contact, new_contact, edit_contact,get_customer_name
from hycrm.views import main_sale_opportunity,new_sale_opportunity,edit_sale_opportunity
from hycrm.views import main_project_apply
from hycrm.views import main_weekly_plan
from hycrm.views import main_travel_request
from hycrm.views import main_travel_report
from hycrm.views import main_budget_apply
from hycrm.views import main_business_apply
from hycrm.views import main_sale_report

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       ('^$', index),
                       (r'^crm/$', main_view),
                       (r'^crm/main_page/$', main_page),

                       (r'^crm/main_customer/$', main_customer),
                       (r'^crm/main_customer/new_customer$', new_customer),
                       (r'^crm/main_customer/edit_customer$', edit_customer),

                       (r'^crm/main_contact/$', main_contact),
                       (r'^crm/main_contact/new_contact', new_contact),
                       (r'^crm/main_contact/edit_contact', edit_contact),
                       (r'^crm/main_contact/all_customers', get_customer_name),

                       (r'^crm/main_sale_opportunity/$', main_sale_opportunity),
                       (r'^crm/main_sale_opportunity/new_sale_opportunity', new_sale_opportunity),
                       (r'^crm/main_sale_opportunity/edit_sale_opportunity', edit_sale_opportunity),

                       (r'^crm/main_project_apply/$', main_project_apply),
                       (r'^crm/main_weekly_plan/$', main_weekly_plan),
                       (r'^crm/main_travel_request/$', main_travel_request),
                       (r'^crm/main_travel_report/$', main_travel_report),
                       (r'^crm/main_budget_apply/$', main_budget_apply),
                       (r'^crm/main_business_apply/$', main_business_apply),
                       (r'^crm/main_sale_report/$', main_sale_report),
)

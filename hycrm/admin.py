__author__ = 'ThinkPad'
from django.contrib import admin
from hycrm.models import Customer,Contact,Sale_opportunity
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Sale_opportunity)

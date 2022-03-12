from django.contrib import admin

from .models import Customer,CreditProvider

admin.site.register(CreditProvider)
admin.site.register(Customer)
from django.contrib import admin

from .models import Customer,CreditProvider



class CreditData(admin.ModelAdmin):
    readonly_fields=('credit',)



admin.site.register(CreditProvider,CreditData)
admin.site.register(Customer,CreditData)
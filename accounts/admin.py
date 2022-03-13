from django.contrib import admin

from .models import Customer,CreditProvider,CustomUser



class CreditDataAdmin(admin.ModelAdmin):
    readonly_fields=('credit',)



admin.site.register(CreditProvider,CreditDataAdmin)
admin.site.register(Customer,CreditDataAdmin)


class SuperUserAdmin(CreditDataAdmin):

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_superuser=True)

admin.site.register(CustomUser,SuperUserAdmin)
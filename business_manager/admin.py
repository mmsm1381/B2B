from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import SysTransaction

User = get_user_model()


class TransactionAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider": 
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        if db_field.name == "consumer":
            kwargs["queryset"] = User.objects.filter(is_superuser=False).exclude(id=request.user.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return SysTransaction.objects.filter(Q(provider=request.user)|Q(consumer=request.user))


admin.site.register(SysTransaction,TransactionAdmin)





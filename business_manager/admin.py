from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import SysTransaction,Wallet

User = get_user_model()


class TransactionAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "provider": 
            kwargs["queryset"] = Wallet.objects.filter(owner=request.user)
        if db_field.name == "consumer":
            kwargs["queryset"] = Wallet.objects.exclude(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return SysTransaction.objects.filter(Q(provider=request.user.wallet)|Q(consumer=request.user.wallet))


admin.site.register(SysTransaction,TransactionAdmin)


class WalletAdmin(admin.ModelAdmin):
    
    readonly_fields = ('credit',)


admin.site.register(Wallet,WalletAdmin)


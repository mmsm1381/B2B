from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self) -> None:
        from .groups import create_credit_provider_group 
        from .signals import give_per_to_credit_provider
        create_credit_provider_group()
        return super().ready()
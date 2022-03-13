from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self) -> None:
        from .groups import create_staff_group 
        from .signals import wallet_creation_and_give_intinal_permisons_to_staff
        return super().ready()
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from business_manager.models import Wallet

User = get_user_model()


@receiver(post_save, sender=User)
def wallet_creation_and_give_intinal_permisons_to_staff(sender, instance, created, **kwargs):

    if created:
        Wallet.objects.create(owner=instance)

        if instance.is_superuser==False and  instance.is_staff == True:
            credit_provider_group = Group.objects.get(name='credit_provider')
            credit_provider_group.add(instance)
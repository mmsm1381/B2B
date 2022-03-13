from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group

from .models import CreditProvider


@receiver(post_save, sender=CreditProvider)
def give_per_to_credit_provider(sender, instance, created, **kwargs):

    if created:
        credit_provider_group = Group.objects.get(name='credit_provider')
        credit_provider_group.user_set.add(instance) 
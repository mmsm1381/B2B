from django.contrib.auth.models import Group, Permission

def create_credit_provider_group():
    new_group, created = Group.objects.get_or_create(name='credit_provider')

    add_taransaction_per = Permission.objects.get(codename="add_systransaction")
    view_taransaction_per = Permission.objects.get(codename="view_systransaction")
    new_group.permissions.add(add_taransaction_per)
    new_group.permissions.add(view_taransaction_per)
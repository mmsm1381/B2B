# Generated by Django 4.0.3 on 2022-03-11 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systransaction',
            name='consumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incoming_Transaction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='systransaction',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_Transaction', to=settings.AUTH_USER_MODEL),
        ),
    ]

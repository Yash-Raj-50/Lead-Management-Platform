# Generated by Django 4.0.2 on 2022-03-19 12:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0026_alter_lead_created_at_alter_siteuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 18, 9, 54, 420187), verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Manager_is',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Manager', to=settings.AUTH_USER_MODEL, verbose_name='Manage_id'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 18, 9, 54, 421388), verbose_name='date_created'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-19 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0020_alter_lead_created_at_alter_siteuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 16, 41, 1, 160495), verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 16, 41, 1, 161002), verbose_name='date_created'),
        ),
    ]
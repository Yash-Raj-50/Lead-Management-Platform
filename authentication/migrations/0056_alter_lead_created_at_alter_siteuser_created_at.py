# Generated by Django 4.0.2 on 2022-03-26 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0055_alter_lead_created_at_alter_siteuser_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 18, 11, 5, 24159), verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 18, 11, 5, 24159), verbose_name='date_created'),
        ),
    ]

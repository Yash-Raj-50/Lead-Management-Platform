# Generated by Django 4.0.2 on 2022-03-08 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_siteuser_created_at_alter_siteuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 8, 19, 5, 52, 670599), verbose_name='date_created'),
        ),
    ]

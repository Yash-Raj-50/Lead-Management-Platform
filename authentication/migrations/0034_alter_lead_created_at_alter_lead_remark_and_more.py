# Generated by Django 4.0.2 on 2022-03-24 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0033_lead_remark_alter_lead_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 25, 0, 37, 29, 697411), verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='lead',
            name='remark',
            field=models.TextField(default='Add+'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 25, 0, 37, 29, 698040), verbose_name='date_created'),
        ),
    ]
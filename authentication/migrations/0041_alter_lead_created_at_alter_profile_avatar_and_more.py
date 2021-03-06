# Generated by Django 4.0.2 on 2022-03-26 06:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0040_alter_lead_created_at_alter_profile_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 12, 14, 30, 648692), verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='profile.png', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 12, 14, 30, 649272), verbose_name='date_created'),
        ),
    ]

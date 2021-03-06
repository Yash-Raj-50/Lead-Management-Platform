# Generated by Django 4.0.2 on 2022-03-26 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0038_profile_avatar_alter_lead_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 11, 45, 39, 62782), verbose_name='date_created'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='static/profile.png', upload_to='static/userImages/'),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 26, 11, 45, 39, 63382), verbose_name='date_created'),
        ),
    ]

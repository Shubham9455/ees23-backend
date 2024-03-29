# Generated by Django 3.2.7 on 2022-11-04 07:49

import custom_auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_auto_20221103_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='referral_code',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='referral_count',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='user_referral_code',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[custom_auth.models.isValid]),
        ),
    ]

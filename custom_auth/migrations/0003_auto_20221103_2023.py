# Generated by Django 3.2.7 on 2022-11-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_auto_20221103_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='college_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='user_referral_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='year',
            field=models.CharField(choices=[('ONE', '1st year'), ('TWO', '2nd year'), ('THREE', '3rd year'), ('FOUR', '4th year')], max_length=20),
        ),
    ]
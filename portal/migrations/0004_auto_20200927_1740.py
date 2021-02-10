# Generated by Django 2.1.7 on 2020-09-27 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20200927_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=13)),
                ('OTP', models.CharField(max_length=4)),
                ('Time', models.DateTimeField(default=datetime.datetime(2020, 9, 27, 17, 40, 12, 699330))),
            ],
        ),
        migrations.DeleteModel(
            name='mobile_otp',
        ),
    ]

# Generated by Django 2.1.7 on 2020-09-27 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20200927_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileotp',
            name='Time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 27, 17, 58, 0, 456262)),
        ),
        migrations.AlterField(
            model_name='mobileotp',
            name='mobile_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]

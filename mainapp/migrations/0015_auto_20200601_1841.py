# Generated by Django 3.0.6 on 2020-06-01 15:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20200601_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 18, 41, 50, 10620)),
        ),
    ]

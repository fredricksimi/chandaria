# Generated by Django 3.0.6 on 2020-06-01 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20200601_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 19, 25, 44, 471982)),
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-02 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20200601_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 7, 35, 25, 220599)),
        ),
    ]

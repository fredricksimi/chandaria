# Generated by Django 3.0.6 on 2020-06-02 04:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20200602_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 7, 41, 43, 403983)),
        ),
    ]
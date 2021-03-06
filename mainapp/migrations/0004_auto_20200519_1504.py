# Generated by Django 3.0.6 on 2020-05-19 12:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20200517_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenges',
            name='status',
        ),
        migrations.AddField(
            model_name='challenges',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='challenges',
            name='is_in_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='challenges',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 18, 15, 4, 47, 709262)),
        ),
    ]

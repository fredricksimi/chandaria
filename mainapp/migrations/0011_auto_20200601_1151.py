# Generated by Django 3.0.6 on 2020-06-01 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20200601_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 11, 51, 43, 531890)),
        ),
        migrations.RemoveField(
            model_name='preapproved_challenge',
            name='tags',
        ),
        migrations.AddField(
            model_name='preapproved_challenge',
            name='tags',
            field=models.ManyToManyField(to='mainapp.ChallengeTag'),
        ),
    ]

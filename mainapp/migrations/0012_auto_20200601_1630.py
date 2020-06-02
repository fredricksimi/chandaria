# Generated by Django 3.0.6 on 2020-06-01 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200601_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='image',
            field=models.ImageField(blank=True, default='default-banner.jpg', upload_to='media_pics/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 16, 30, 16, 328220)),
        ),
    ]

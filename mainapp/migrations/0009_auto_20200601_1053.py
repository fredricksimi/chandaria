# Generated by Django 3.0.6 on 2020-06-01 07:53

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20200529_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='open_until',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 10, 53, 44, 332364)),
        ),
        migrations.AlterField(
            model_name='challenges',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Energy', 'Energy'), ('Lifestyle', 'Lifestyle'), ('Technology', 'Technology'), ('Culture', 'Culture'), ('Fashion', 'Fashion'), ('Entertainment', 'Entertainment'), ('Agriculture', 'Agriculture'), ('Governance', 'Governance'), ('Health', 'Health')], max_length=120),
        ),
        migrations.AlterField(
            model_name='preapproved_challenge',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Energy', 'Energy'), ('Lifestyle', 'Lifestyle'), ('Technology', 'Technology'), ('Culture', 'Culture'), ('Fashion', 'Fashion'), ('Entertainment', 'Entertainment'), ('Agriculture', 'Agriculture'), ('Governance', 'Governance'), ('Health', 'Health')], max_length=120),
        ),
    ]

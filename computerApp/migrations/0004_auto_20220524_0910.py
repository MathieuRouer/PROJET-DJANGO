# Generated by Django 2.2.25 on 2022-05-24 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0003_auto_20220524_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 24, 9, 10, 55, 158006)),
        ),
    ]

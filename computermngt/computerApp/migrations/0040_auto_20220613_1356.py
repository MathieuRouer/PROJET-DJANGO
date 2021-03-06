# Generated by Django 2.2.25 on 2022-06-13 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0039_auto_20220613_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='employe',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=15)),
                ('prenom', models.CharField(max_length=15)),
                ('date_recrutement', models.DateField(default=datetime.datetime(2022, 6, 13, 13, 56, 26, 14423))),
            ],
        ),
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 6, 13, 13, 56, 26, 14054)),
        ),
    ]

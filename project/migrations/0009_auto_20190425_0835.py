# Generated by Django 2.0 on 2019-04-25 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20190425_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 4, 25, 3, 5, 27, 895851)),
        ),
    ]
# Generated by Django 2.0 on 2019-05-08 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20190507_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 5, 8, 5, 35, 4, 71754)),
        ),
    ]

# Generated by Django 2.0 on 2019-05-07 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_auto_20190506_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 5, 7, 12, 35, 13, 884606)),
        ),
    ]
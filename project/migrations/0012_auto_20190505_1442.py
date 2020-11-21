# Generated by Django 2.0 on 2019-05-05 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20190425_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], default='available', max_length=22),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 5, 5, 9, 12, 53, 461417)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=22),
        ),
    ]
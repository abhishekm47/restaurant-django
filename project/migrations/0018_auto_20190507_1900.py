# Generated by Django 2.0 on 2019-05-07 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20190507_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5, max_length=22),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='time',
            field=models.TimeField(default=datetime.datetime(2019, 5, 7, 13, 30, 48, 735782)),
        ),
    ]

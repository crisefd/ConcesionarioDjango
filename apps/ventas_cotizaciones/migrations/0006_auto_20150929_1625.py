# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_cotizaciones', '0005_auto_20150929_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 9, 29, 16, 25, 57, 841394, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 9, 29, 16, 25, 57, 839494, tzinfo=utc)),
        ),
    ]

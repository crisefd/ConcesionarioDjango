# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizaciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 9, 26, 19, 33, 59, 368822, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='ventas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 9, 26, 19, 33, 59, 366930, tzinfo=utc)),
        ),
    ]

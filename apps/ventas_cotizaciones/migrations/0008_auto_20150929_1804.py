# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_cotizaciones', '0007_auto_20150929_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 9, 29, 18, 4, 49, 979675, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 9, 29, 18, 4, 49, 977687, tzinfo=utc)),
        ),
    ]

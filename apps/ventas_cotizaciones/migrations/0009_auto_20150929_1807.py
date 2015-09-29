# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_cotizaciones', '0008_auto_20150929_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizaciones',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

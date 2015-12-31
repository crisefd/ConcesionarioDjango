# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0002_sucursales_is_active'),
        ('ventas_cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='sucursal',
            field=models.ForeignKey(default=b'', to='sucursales.Sucursales'),
        ),
    ]

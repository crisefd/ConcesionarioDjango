# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0002_sucursales_is_active'),
        ('ventas_cotizaciones', '0002_ventas_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizaciones',
            name='doc_id_comprador',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='sucursal',
            field=models.ForeignKey(default=b'', to='sucursales.Sucursales'),
        ),
    ]

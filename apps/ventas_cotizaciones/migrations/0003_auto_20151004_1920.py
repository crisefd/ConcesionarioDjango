# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_cotizaciones', '0002_auto_20151004_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='automovil',
            field=models.ForeignKey(to='inventario.Automovil'),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='doc_id_comprador',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]

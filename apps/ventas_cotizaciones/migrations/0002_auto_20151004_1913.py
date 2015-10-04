# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas_cotizaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotizaciones',
            old_name='automovil_fk',
            new_name='automovil',
        ),
        migrations.RenameField(
            model_name='cotizaciones',
            old_name='vendedor_fk',
            new_name='vendedor',
        ),
        migrations.RenameField(
            model_name='ventas',
            old_name='automovil_fk',
            new_name='automovil',
        ),
        migrations.RenameField(
            model_name='ventas',
            old_name='vendedor_fk',
            new_name='vendedor',
        ),
    ]

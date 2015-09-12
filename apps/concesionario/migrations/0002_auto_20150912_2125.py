# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('concesionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='vendedor_fk',
            field=models.ForeignKey(to='usuarios.Vendedor'),
        ),
        migrations.AddField(
            model_name='ordenes_trabajo',
            name='jefe_taller_fk',
            field=models.ForeignKey(to='usuarios.Jefe_Taller'),
        ),
        migrations.AddField(
            model_name='ordenes_trabajo',
            name='mecanico_asignado',
            field=models.ForeignKey(to='concesionario.Mecanicos'),
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='automovil_fk',
            field=models.ForeignKey(to='concesionario.Automovil'),
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='vendedor_fk',
            field=models.ForeignKey(to='usuarios.Vendedor'),
        ),
    ]

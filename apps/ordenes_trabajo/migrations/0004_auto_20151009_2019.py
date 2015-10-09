# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
        ('ordenes_trabajo', '0003_auto_20151009_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden_Repuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Orden_Repuesto',
                'verbose_name_plural': 'Orden_Repuestos',
            },
        ),
        migrations.AddField(
            model_name='ordenes_trabajo',
            name='costo',
            field=models.FloatField(default=500),
        ),
        migrations.AlterField(
            model_name='ordenes_trabajo',
            name='estado',
            field=models.CharField(default=b'Activa', max_length=50, choices=[(b'Activa', b'Activa'), (b'Cancelada', b'Cancelada'), (b'Finalizada', b'Finalizada')]),
        ),
        migrations.AddField(
            model_name='orden_repuesto',
            name='orden',
            field=models.ForeignKey(to='ordenes_trabajo.Ordenes_Trabajo'),
        ),
        migrations.AddField(
            model_name='orden_repuesto',
            name='repuesto',
            field=models.ForeignKey(to='inventario.Repuesto'),
        ),
    ]

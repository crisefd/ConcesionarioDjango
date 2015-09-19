# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('serial_id', models.CharField(default=b'0000', max_length=50, serialize=False, primary_key=True)),
                ('precio', models.FloatField(default=0.0)),
                ('marca', models.CharField(default=b'Acme', max_length=50)),
                ('modelo', models.CharField(default=b'Acme', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cotizaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_comprador', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mecanicos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=50)),
                ('apellido', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes_Trabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=150, null=True)),
                ('matricula_vehiculo', models.CharField(max_length=10, unique=True, null=True)),
                ('estado', models.CharField(default=b'Activa', max_length=50, choices=[(b'Activa', b'Activa'), (b'CANCELADA', b'Cancelada'), (b'FINALIZADA', b'Finalizada')])),
            ],
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('serial_id', models.CharField(default=b'0000', max_length=50, serialize=False, primary_key=True)),
                ('precio', models.FloatField(default=0.0)),
                ('nombre', models.CharField(default=b'', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=50)),
                ('direccion', models.CharField(default=b'', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_comprador', models.CharField(default=b'', max_length=50)),
                ('doc_id_comprador', models.CharField(default=b'00000000', unique=True, max_length=50)),
                ('valor_venta', models.FloatField(default=0.0)),
                ('automovil_fk', models.ForeignKey(to='concesionario.Automovil', null=True)),
            ],
        ),
    ]

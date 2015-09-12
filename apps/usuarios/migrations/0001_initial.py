# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concesionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('passwd', models.CharField(max_length=30, null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('genero', models.CharField(max_length=1, null=True)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True, null=True)),
                ('numero_telefono', models.CharField(max_length=50, unique=True, null=True)),
                ('direccion_residencia', models.CharField(max_length=50, unique=True, null=True)),
                ('documento_id', models.CharField(max_length=30, serialize=False, primary_key=True, blank=True)),
                ('esta_activo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jefe_Taller',
            fields=[
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('passwd', models.CharField(max_length=30, null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('genero', models.CharField(max_length=1, null=True)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True, null=True)),
                ('numero_telefono', models.CharField(max_length=50, unique=True, null=True)),
                ('direccion_residencia', models.CharField(max_length=50, unique=True, null=True)),
                ('documento_id', models.CharField(max_length=30, serialize=False, primary_key=True, blank=True)),
                ('esta_activo', models.BooleanField(default=True)),
                ('sucursal_fk', models.ForeignKey(to='concesionario.Sucursales')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('nombre', models.CharField(max_length=50, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('passwd', models.CharField(max_length=30, null=True)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('genero', models.CharField(max_length=1, null=True)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True, null=True)),
                ('numero_telefono', models.CharField(max_length=50, unique=True, null=True)),
                ('direccion_residencia', models.CharField(max_length=50, unique=True, null=True)),
                ('documento_id', models.CharField(max_length=30, serialize=False, primary_key=True, blank=True)),
                ('esta_activo', models.BooleanField(default=True)),
                ('num_ventas', models.PositiveIntegerField(default=0)),
                ('sucursal_fk', models.ForeignKey(to='concesionario.Sucursales')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

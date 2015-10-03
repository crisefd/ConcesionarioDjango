# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                ('descripcion', models.TextField(max_length=350, null=True)),
                ('matricula_vehiculo', models.CharField(max_length=10, unique=True, null=True)),
                ('estado', models.CharField(default=b'ACTIVA', max_length=50, choices=[(b'ACTIVA', b'Activa'), (b'CANCELADA', b'Cancelada'), (b'FINALIZADA', b'Finalizada')])),
            ],
        ),
    ]

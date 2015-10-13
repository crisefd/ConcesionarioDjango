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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField(default=0.0)),
                ('disponible', models.BooleanField(default=True)),
                ('marca', models.CharField(default=b'Acme', max_length=50)),
                ('modelo', models.CharField(default=b'Acme', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField(default=0.0)),
                ('disponible', models.BooleanField(default=True)),
                ('nombre', models.CharField(default=b'', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

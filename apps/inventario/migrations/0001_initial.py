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
    ]

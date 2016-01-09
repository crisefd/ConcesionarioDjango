# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20151218_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='marca',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='automovil',
            name='marca',
            field=models.CharField(default=b'', max_length=50),
        ),
        migrations.AlterField(
            model_name='automovil',
            name='modelo',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]

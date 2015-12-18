# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automovil',
            name='disponible',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='disponible',
        ),
        migrations.AddField(
            model_name='automovil',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]

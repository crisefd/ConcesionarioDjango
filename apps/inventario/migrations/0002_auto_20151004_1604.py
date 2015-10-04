# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automovil',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]

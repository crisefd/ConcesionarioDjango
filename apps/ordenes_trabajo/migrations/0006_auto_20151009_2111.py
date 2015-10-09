# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_trabajo', '0005_auto_20151009_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenes_trabajo',
            name='matricula_vehiculo',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

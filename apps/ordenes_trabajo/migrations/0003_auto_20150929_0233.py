# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_trabajo', '0002_auto_20150926_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenes_trabajo',
            name='descripcion',
            field=models.TextField(max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='ordenes_trabajo',
            name='estado',
            field=models.CharField(default=b'ACTIVA', max_length=50, choices=[(b'ACTIVA', b'Activa'), (b'CANCELADA', b'Cancelada'), (b'FINALIZADA', b'Finalizada')]),
        ),
    ]

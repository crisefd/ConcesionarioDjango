# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_trabajo', '0006_auto_20151009_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden_repuesto',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

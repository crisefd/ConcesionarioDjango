# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ordenes_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenes_trabajo',
            name='jefe_taller_fk',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordenes_trabajo',
            name='mecanico_asignado',
            field=models.ForeignKey(to='ordenes_trabajo.Mecanicos'),
        ),
    ]

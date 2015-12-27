# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_trabajo', '0002_auto_20151008_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordenes_trabajo',
            old_name='jefe_taller_fk',
            new_name='jefe_taller',
        ),
    ]

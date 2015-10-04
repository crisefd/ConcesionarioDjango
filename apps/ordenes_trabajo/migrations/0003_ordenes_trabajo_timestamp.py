# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenes_trabajo', '0002_auto_20151003_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenes_trabajo',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

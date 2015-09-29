# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_auto_20150929_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, to='sucursales.Sucursales', null=True),
        ),
    ]

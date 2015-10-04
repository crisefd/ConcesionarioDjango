# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0001_initial'),
        ('usuarios', '0003_auto_20151003_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, to='sucursales.Sucursales', null=True),
        ),
    ]

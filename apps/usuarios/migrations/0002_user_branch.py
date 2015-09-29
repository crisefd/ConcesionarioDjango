# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sucursales', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(default=b'', to='sucursales.Sucursales'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(to='sucursales.Sucursales', null=True),
        ),
    ]

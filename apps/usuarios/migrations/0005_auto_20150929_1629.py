# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20150929_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20150929_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
    ]

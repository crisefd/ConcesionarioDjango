# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_user_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jefetaller_sucursal',
            name='jefe_fk',
        ),
        migrations.RemoveField(
            model_name='jefetaller_sucursal',
            name='sucursal_fk',
        ),
        migrations.RemoveField(
            model_name='vendedor_sucursal',
            name='sucursal_fk',
        ),
        migrations.RemoveField(
            model_name='vendedor_sucursal',
            name='vendedor_fk',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.DeleteModel(
            name='JefeTaller_Sucursal',
        ),
        migrations.DeleteModel(
            name='Vendedor_Sucursal',
        ),
    ]

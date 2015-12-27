# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cotizaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_comprador', models.CharField(default=b'', max_length=50)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('automovil', models.ForeignKey(to='inventario.Automovil')),
                ('vendedor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_comprador', models.CharField(default=b'', max_length=50)),
                ('doc_id_comprador', models.CharField(default=b'', max_length=50)),
                ('valor_venta', models.FloatField(default=0.0)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('automovil', models.ForeignKey(to='inventario.Automovil')),
                ('vendedor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

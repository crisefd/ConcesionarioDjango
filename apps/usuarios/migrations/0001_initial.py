# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('concesionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address', db_index=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birth_date', models.DateField(blank=True)),
                ('sex', models.CharField(default=b'', max_length=1)),
                ('address', models.CharField(default=b'', max_length=50)),
                ('phone_number', models.CharField(default=b'', max_length=50)),
                ('id_document', models.CharField(max_length=50, serialize=False, primary_key=True, blank=True)),
                ('staff_type', models.CharField(default=b'', max_length=50)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='JefeTaller_Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jefe_fk', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('sucursal_fk', models.ForeignKey(to='concesionario.Sucursales')),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor_Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sucursal_fk', models.ForeignKey(to='concesionario.Sucursales')),
                ('vendedor_fk', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

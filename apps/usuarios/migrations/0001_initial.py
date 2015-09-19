# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import apps.usuarios.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('concesionario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80, verbose_name='name')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            managers=[
                ('objects', apps.usuarios.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='JefeTaller_Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission_',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('codename', models.CharField(max_length=100, verbose_name='codename')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', to_field=django.db.models.deletion.CASCADE, verbose_name='content type')),
            ],
            options={
                'ordering': ('content_type__app_label', 'content_type__model', 'codename'),
                'verbose_name': 'permission',
                'verbose_name_plural': 'permissions',
            },
            managers=[
                ('objects', apps.usuarios.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(max_length=50, blank=True)),
                ('apellido', models.CharField(max_length=50, blank=True)),
                ('passwd', models.CharField(max_length=30, blank=True)),
                ('fecha_nacimiento', models.DateField(blank=True)),
                ('genero', models.CharField(max_length=1, blank=True)),
                ('correo_electronico', models.EmailField(unique=True, max_length=254, blank=True)),
                ('numero_telefono', models.CharField(unique=True, max_length=50, blank=True)),
                ('direccion_residencia', models.CharField(unique=True, max_length=50, blank=True)),
                ('documento_id', models.CharField(max_length=30, serialize=False, primary_key=True, blank=True)),
                ('esta_activo', models.BooleanField(default=True)),
                ('tipo', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='usuarios.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='usuarios.Permission_', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Vendedor_Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sucursal_fk', models.ForeignKey(to='concesionario.Sucursales')),
                ('vendedor_fk', models.ForeignKey(to='usuarios.User')),
            ],
        ),
        migrations.AddField(
            model_name='jefetaller_sucursal',
            name='jefe_fk',
            field=models.ForeignKey(to='usuarios.User'),
        ),
        migrations.AddField(
            model_name='jefetaller_sucursal',
            name='sucursal_fk',
            field=models.ForeignKey(to='concesionario.Sucursales'),
        ),
        migrations.AddField(
            model_name='group',
            name='permissions',
            field=models.ManyToManyField(to='usuarios.Permission_', verbose_name='permissions', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='permission_',
            unique_together=set([('content_type', 'codename')]),
        ),
    ]

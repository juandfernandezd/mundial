# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-04 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0005_auto_20180403_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participante',
            old_name='es_creado',
            new_name='es_admin',
        ),
        migrations.AlterField(
            model_name='participante',
            name='posicion',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participante',
            name='puntaje',
            field=models.FloatField(default=0.0),
        ),
    ]
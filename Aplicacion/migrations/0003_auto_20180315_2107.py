# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-16 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_auto_20180315_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='goles_local',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='partido',
            name='goles_visitante',
            field=models.IntegerField(default=-1),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-03 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0004_partido_finalizado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='equipo_favorito',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='Aplicacion.Equipo'),
        ),
    ]

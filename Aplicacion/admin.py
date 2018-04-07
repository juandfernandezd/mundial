# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Aplicacion.models import Partido, Equipo, Grupo, Participante, Invitacion,\
    Ronda, Pronostico
    
admin.site.site_header = "Mundial"
admin.site.site_title = "Mundial"
    
class PartidoAdminView(admin.ModelAdmin):
    list_display = ('id','equipo_local','goles_local','equipo_visitante','goles_visitante','fecha','ronda')

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Grupo)
admin.site.register(Participante)
admin.site.register(Invitacion)
admin.site.register(Ronda)
admin.site.register(Partido, PartidoAdminView)
admin.site.register(Pronostico)
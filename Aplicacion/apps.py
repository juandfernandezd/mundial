# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class AplicacionConfig(AppConfig):
    name = 'Aplicacion'
    
    def ready(self):
        import Aplicacion.signals

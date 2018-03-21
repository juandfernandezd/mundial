# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Aplicacion.models import Equipo
from Aplicacion.ApiRest.serializers import EquipoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

# Create your views here.

class ObtenerEquipos(APIView):
    
    equipo_serializer = EquipoSerializer
    
    def get(self, request):
        equipos = Equipo.objects.all()
        respuesta = self.equipo_serializer(equipos, many = True)
        return Response(respuesta.data, status = status.HTTP_200_OK)

obtener_equipos = ObtenerEquipos.as_view()

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    
facebook_login = FacebookLogin.as_view()

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

google_login = GoogleLogin.as_view()

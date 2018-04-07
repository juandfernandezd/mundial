# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Aplicacion.models import Equipo, Grupo, Participante
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


class MarcarEquipoFavorito(APIView):
    
    def post(self, request):
        
        if request.data:
            id_equipo = request.data['id_equipo']
            equipo = Equipo.objects.filter(id = id_equipo)
            request.user.perfil.asignar_equipo_favorito(equipo[0])
            return Response({"mensaje":"Se ha marcado el equipo favorito"}, status = status.HTTP_200_OK)
        else:
            return Response({"mensaje":"No se han proporcionado los parametros necesarios"}, status = status.HTTP_400_BAD_REQUEST)
        
marcar_equipo_favorito = MarcarEquipoFavorito.as_view()

class RegistrarGrupo(APIView):
    
    def post(self, request):
        
        if request.data:
            nombre = request.data['nombre']
            apuesta = request.data['apuesta']
            categoria = request.data['categoria']
            tipo = request.data['tipo']
            chat = request.data['chat']
            grupo = Grupo.create(nombre, apuesta, categoria, tipo, chat, request.user)
            Participante.create(request.user, grupo, True)
            
            return Response({"mensaje":"Se ha registrado el grupo " + grupo.nombre}, status = status.HTTP_200_OK)
        
        else:
            return Response({"mensaje":"No se han proporcionado los parametros necesarios"}, status = status.HTTP_400_BAD_REQUEST)
        
registrar_grupo = RegistrarGrupo.as_view()


class ObtenerGrupos(APIView):
    
    def post(self, request):
        
        if request.data:
            
            participantes = Participante.objects.filter(usuario = request.user.id)
            print participantes
            return Response({"mensaje":"bien"}, status = status.HTTP_200_OK)
        
        else:
            return Response({"mensaje":"No se han proporcionado los parametros necesarios"}, status = status.HTTP_400_BAD_REQUEST)
        
obtener_grupos = ObtenerGrupos.as_view()



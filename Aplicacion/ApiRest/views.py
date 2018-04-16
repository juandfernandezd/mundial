# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Aplicacion.models import Equipo, Grupo, Participante, Partido
from Aplicacion.ApiRest.serializers import EquipoSerializer, PartidoSerializer,\
    GrupoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

import base64

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
            
            participantes = Participante.objects.filter(usuario = request.user.id, es_admin = True)
            
            if ((len(participantes) < 2 and request.user.perfil.es_premium == False) or request.user.perfil.es_premium == True): 
                
                nombre = request.data['nombre']
                apuesta = request.data['apuesta']
                categoria = request.data['categoria']
                tipo = request.data['tipo']
                chat = request.data['chat']
                id_partido = request.data['id_partido']
                grupo = Grupo.create(nombre, apuesta, categoria, tipo, chat)
                # Se debe enviar el codigo base64 de la imagen desde el / despues de la palabra base64,
                imgdata = base64.b64decode(request.data['imagen'])
                filename = str(grupo.id) + ".jpg"
                print filename
                with open("../media_cdn/"+filename, 'wb') as f:
                    f.write(imgdata)
                f.close()
                grupo.asignar_imagen(filename)
                
                Participante.create(request.user, grupo, True)
                partido = Partido.objects.filter(id = id_partido)
                grupo.partidos.add(partido[0])
            
                return Response({"mensaje":"Se ha registrado el grupo " + grupo.nombre}, status = status.HTTP_200_OK)
            
            else:
                return Response({"mensaje":"Ha superado el numero maximo de grupos permitidos en version free"}, status = status.HTTP_401_UNAUTHORIZED)
        
        else:
            return Response({"mensaje":"No se han proporcionado los parametros necesarios"}, status = status.HTTP_400_BAD_REQUEST)
        
registrar_grupo = RegistrarGrupo.as_view()


class ObtenerGrupos(APIView):
    
    grupo_serializer = GrupoSerializer
    
    def get(self, request):
        
        participantes = Participante.objects.filter(usuario = request.user.id)
        grupos = []
        for participante in participantes:
            grupos.append(participante.grupo)
                
        respuesta = self.grupo_serializer(grupos, many = True)
        return Response(respuesta.data, status = status.HTTP_200_OK)
        
obtener_grupos = ObtenerGrupos.as_view()

class ObtenerPartidos(APIView):
    
    partido_serializer = PartidoSerializer
    
    def get(self, request):
        
        partidos = Partido.objects.filter(finalizado = False)
        respuesta = self.partido_serializer(partidos, many = True)
        return Response(respuesta.data, status = status.HTTP_200_OK)
        
obtener_partidos = ObtenerPartidos.as_view()

class VerificarPremium(APIView):
    
    def get(self, request):
        
        if (request.user.perfil.es_premium == True):
            return Response({"mensaje":"El usuario es premium","valor":1}, status = status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El usuario es free","valor":0}, status = status.HTTP_200_OK)
        
verificar_premium = VerificarPremium.as_view()


class ObtenerEquipoFavorito(APIView):
    
    equipo_serializer = EquipoSerializer
    
    def get(self, request):
        
        equipo = request.user.perfil.equipo_favorito
        respuesta = self.equipo_serializer(equipo, many = False)
        return Response(respuesta.data, status = status.HTTP_200_OK)
    
obtener_equipo_favorito = ObtenerEquipoFavorito.as_view()


class ModificarPremium(APIView):
    
    def post(self, request):
        
        request.user.perfil.modificar_premium()
        return Response({"mensaje":"El usuario " + request.user.username + " ahora es premium"}, status = status.HTTP_200_OK)
    
modificar_premium = ModificarPremium.as_view()
            




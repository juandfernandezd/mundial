# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
    
    nombre = models.CharField(max_length = 100)
    logo = models.ImageField()
    
    def __unicode__(self):
        return self.nombre
    
class Perfil(models.Model):
    
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    equipo_favorito = models.ForeignKey(Equipo, related_name = 'usuario', blank = True, null = True)
    es_premium = models.BooleanField(default = False)
    
    @classmethod
    def create(cls, usuario):
        perfil = cls(usuario = usuario)
        perfil.save()
        return perfil
        
    def asignar_equipo_favorito(self, equipo):
        self.equipo_favorito = equipo
        self.save()
        
    def modificar_premium(self):
        self.es_premium = True
        self.save()
        
    
class Ronda(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    def __unicode__(self):
        return self.nombre
    
class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipo, related_name = 'Local')
    equipo_visitante = models.ForeignKey(Equipo, related_name = 'Visitante')
    fecha = models.DateTimeField()
    goles_local = models.IntegerField(default = -1)
    goles_visitante = models.IntegerField(default = -1)
    ronda = models.ForeignKey(Ronda)
    finalizado = models.BooleanField(default = False)
    
    def __unicode__(self):
        return '{0} VS {1}'.format(self.equipo_local.nombre, self.equipo_visitante.nombre)

class Grupo(models.Model):
    
    PUBLICO = 'Publico'
    PRIVADO = 'Privado'
    CATEGORIAS = ((PUBLICO,'Publico'),(PRIVADO,'Privado'),)
    
    SIMPLE = 'Simple'
    MULTIPLE = 'Multiple'
    TIPOS = ((SIMPLE,'Simple'),(MULTIPLE,'Multiple'),)

    nombre = models.CharField(max_length = 50)
    apuesta = models.TextField()
    imagen = models.ImageField(blank = True, null = True)
    categoria = models.CharField(max_length = 8, choices = CATEGORIAS, default = PUBLICO)
    tipo = models.CharField(max_length = 8, choices = TIPOS, default = SIMPLE)
    chat = models.BooleanField(default = False)
    miembros = models.ManyToManyField(User, through = "Participante")
    partidos = models.ManyToManyField(Partido)
    
    @classmethod
    def create(cls, nombre, apuesta, categoria, tipo, chat):
        grupo = cls(nombre = nombre, apuesta = apuesta, categoria = categoria, tipo = tipo, chat = chat)
        grupo.save()
        return grupo
    
    def __unicode__(self):
        return "{0} : {1}".format(self.nombre, self.categoria)
    
    def asignar_imagen(self, ruta):
        self.imagen = ruta
        self.save()
    
class Pronostico(models.Model):
    usuario = models.ForeignKey(User)
    grupo = models.ForeignKey(Grupo)
    partido = models.ForeignKey(Partido)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    
    
class Participante(models.Model):
    
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE)
    puntaje = models.FloatField(default = 0.0)
    posicion = models.IntegerField(default = 0)
    es_admin = models.BooleanField(default = False)
    
    @classmethod
    def create(cls, usuario, grupo, es_admin):
        participante = cls(usuario = usuario, grupo = grupo, es_admin  = es_admin)
        participante.save()
        return participante
    
    def __unicode__(self):
        return self.usuario.username
    
class Invitacion(models.Model):
    usuario = models.ManyToManyField(User)
    mensaje = models.TextField()
    grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE)
    fecha = models.DateTimeField(auto_now = True)
    
    

    
    
    
    


    
    
    



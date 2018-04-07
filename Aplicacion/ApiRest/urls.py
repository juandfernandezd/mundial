from django.conf.urls import url
from Aplicacion.ApiRest.views import obtener_equipos, facebook_login,\
    google_login, marcar_equipo_favorito, registrar_grupo, obtener_grupos


urlpatterns = [
    url(r'^rest-auth/facebook/$',facebook_login),
    url(r'^rest-auth/google/$',google_login),
    url(r'^obtener_equipos/$',obtener_equipos),
    url(r'^marcar_equipo_favorito/$',marcar_equipo_favorito),
    url(r'^registrar_grupo/$',registrar_grupo),
    url(r'^obtener_grupos/$',obtener_grupos),
]
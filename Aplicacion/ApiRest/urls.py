from django.conf.urls import url
from Aplicacion.ApiRest.views import obtener_equipos, facebook_login,\
    google_login, marcar_equipo_favorito, registrar_grupo, obtener_grupos,\
    obtener_partidos, verificar_premium, obtener_equipo_favorito,\
    modificar_premium


urlpatterns = [
    url(r'^rest-auth/facebook/$',facebook_login),
    url(r'^rest-auth/google/$',google_login),
    url(r'^obtener_equipos/$',obtener_equipos),
    url(r'^marcar_equipo_favorito/$',marcar_equipo_favorito),
    url(r'^registrar_grupo/$',registrar_grupo),
    url(r'^obtener_grupos/$',obtener_grupos),
    url(r'^obtener_partidos/$',obtener_partidos),
    url(r'^verificar_premium/$',verificar_premium),
    url(r'^obtener_equipo_favorito/$',obtener_equipo_favorito),
    url(r'^modificar_premium/$',modificar_premium),
]
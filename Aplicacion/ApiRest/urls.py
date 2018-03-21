from django.conf.urls import url
from Aplicacion.ApiRest.views import obtener_equipos, facebook_login,\
    google_login


urlpatterns = [
    url(r'obtener_equipos/$',obtener_equipos),
    url(r'rest-auth/facebook/$',facebook_login),
    url(r'rest-auth/google/$',google_login),
]
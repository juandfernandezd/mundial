from rest_framework.serializers import ModelSerializer
from Aplicacion.models import Equipo

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id','nombre','logo')

from rest_framework.serializers import ModelSerializer
from Aplicacion.models import Equipo, Partido, Ronda, Grupo

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id','nombre','logo')
        
class RondaSerializer(ModelSerializer):
    class Meta:
        model = Ronda
        fields = ('id','fecha_inicio','fecha_fin')
        
class PartidoSerializer(ModelSerializer):
    
    equipo_local = EquipoSerializer(many = False)
    equipo_visitante = EquipoSerializer(many = False)
    ronda = RondaSerializer(many = False)
    
    class Meta:
        model = Partido
        fields = ('id','equipo_local','goles_local','equipo_visitante','goles_visitante','fecha','ronda')
        
class GrupoSerializer(ModelSerializer):
    
    class Meta:
        model = Grupo
        fields = ('id','nombre','apuesta','categoria','imagen')

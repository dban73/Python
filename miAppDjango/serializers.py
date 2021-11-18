from rest_framework import routers, serializers, viewsets
from .models import Persona

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'telefono', 'email']
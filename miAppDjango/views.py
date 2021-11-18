from django.shortcuts import render
from .models import Persona
from .models import Carro

from rest_framework import viewsets
from .serializers import PersonaSerializer
# Create your views here.

def index(request):
    personas = Persona.objects.order_by('nombre')
    context = {
        'titulo_pagina': 'Lista de personas',
        'lista_personas': personas,
    }
    return render(request, 'personas.html',context)

def detail(request, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    context ={
        'titulo_pagina':'Ver Persona',
        'persona': persona,
    }
    return render(request, 'persona.html',context)

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

#Carros
def index2(request):
    carros = Carro.objects.order_by('color')
    context = {
        'titulo_pagina': 'Lista de carros',
        'lista_carros': carros,
    }
    return render(request, 'carros.html',context)

def detail2(request, carro_id):
    carro = Carro.objects.get(pk=carro_id)
    context ={
        'titulo_pagina':'Ver Carro',
        'carro': carro,
    }
    return render(request, 'carro.html',context)
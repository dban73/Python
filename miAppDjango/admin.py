from django.contrib import admin

# Register your models here.
from . models import Persona, Carro

admin.site.register(Persona)
admin.site.register(Carro)
from rest_framework import serializers
from authApp.models.persona import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
         'cc',
         'nombre1',
         'apellido1',
         'fecha',
         'correo',
         'celular'
         ]
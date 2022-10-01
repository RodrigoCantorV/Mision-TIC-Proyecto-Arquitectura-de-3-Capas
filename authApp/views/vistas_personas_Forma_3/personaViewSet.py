from rest_framework import viewsets
from authApp.models.persona import Persona 
from authApp.serializers.personaSerializer import PersonaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
   # permission_classes = [permissions.AllowAny]


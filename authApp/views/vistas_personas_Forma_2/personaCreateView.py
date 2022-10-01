

from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authApp.models.persona import Persona
from authApp.serializers.personaSerializer import PersonaSerializer

  
@api_view(['POST'])
def add_items(request):
    item = PersonaSerializer(data=request.data)
  
    # validating for already existing data
    if Persona.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

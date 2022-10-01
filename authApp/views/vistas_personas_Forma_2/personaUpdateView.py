from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authApp.models.persona import Persona
from authApp.serializers.personaSerializer import PersonaSerializer

@api_view(['POST'])
def update_items(request, pk):
    item = Persona.objects.get(pk=pk)
    data = PersonaSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


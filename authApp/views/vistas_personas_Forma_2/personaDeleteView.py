from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authApp.models.persona import Persona
from authApp.serializers.personaSerializer import PersonaSerializer

@api_view(['DELETE'])
def delete_items(request, pk):
    item = Persona.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)



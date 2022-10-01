
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authApp.models.persona import Persona
from authApp.serializers.personaSerializer import PersonaSerializer

@api_view(['GET'])
def view_items_one(request, pk):
    # checking for the parameters from the URL
    items = Persona.objects.get(pk=pk)
    serializer = PersonaSerializer(items, many=False)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from authApp.models.persona import Persona
from authApp.serializers.personaSerializer import PersonaSerializer

@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    items = Persona.objects.all()
    serializer = PersonaSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


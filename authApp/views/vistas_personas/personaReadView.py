from rest_framework import views, status
from rest_framework import serializers
from rest_framework.response import Response
from authApp.serializers.personaSerializer import PersonaSerializer
from authApp.models.persona import Persona

class PersonaReadView(views.APIView):
    def get(self,request):
          # checking for the parameters from the URL
        items = Persona.objects.all()
        serializer = PersonaSerializer(items, many=True)

        # if there is something in items else raise error
        if items:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

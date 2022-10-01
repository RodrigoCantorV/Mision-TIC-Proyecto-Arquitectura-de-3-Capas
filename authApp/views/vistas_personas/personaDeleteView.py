from rest_framework import views, status
from rest_framework import serializers
from rest_framework.response import Response
from authApp.serializers.personaSerializer import PersonaSerializer
from authApp.models.persona import Persona
from django.http import Http404

class PersonaDeleteView(views.APIView):
    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
           post = self.get_object(pk)
           serializer = PersonaSerializer(post)  
           return Response(serializer.data)
 

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


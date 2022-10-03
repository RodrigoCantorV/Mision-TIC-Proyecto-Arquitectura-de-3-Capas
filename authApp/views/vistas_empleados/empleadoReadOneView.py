from rest_framework import views
from rest_framework.response import Response
from django.http import Http404
from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.models.empleado import Empleado

class EmpleadoReadOneView(views.APIView):
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = EmpleadoSerializer(post)  
        return Response(serializer.data)
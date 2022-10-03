from rest_framework import views, status
from rest_framework.response import Response
from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.models.empleado import Empleado
from django.http import Http404

class EmpleadoDeleteView(views.APIView):
    def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
           post = self.get_object(pk)
           serializer = EmpleadoSerializer(post)  
           return Response(serializer.data)
 

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


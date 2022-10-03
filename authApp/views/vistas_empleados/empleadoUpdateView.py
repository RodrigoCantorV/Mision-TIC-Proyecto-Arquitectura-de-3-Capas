from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.models.empleado import Empleado

class EmpleadoUpdateView(views.APIView):

     def get_object(self, pk):
        try:
            return Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            raise Http404

     def get(self, request, pk, format=None):
           post = self.get_object(pk)
           serializer = EmpleadoSerializer(post)  
           return Response(serializer.data)

     def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = EmpleadoSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
from authApp.serializers.liquidacion_sueldoSerializer import Liquidacion_SueldoSerializer
from authApp.models.liquidacion_sueldo import Liquidacion_Sueldo

class Liquidacion_SueldoUpdateView(views.APIView):

     def get_object(self, pk):
        try:
            return Liquidacion_Sueldo.objects.get(pk=pk)
        except Liquidacion_Sueldo.DoesNotExist:
            raise Http404

     def get(self, request, pk, format=None):
           post = self.get_object(pk)
           serializer = Liquidacion_SueldoSerializer(post)  
           return Response(serializer.data)

     def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = Liquidacion_SueldoSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
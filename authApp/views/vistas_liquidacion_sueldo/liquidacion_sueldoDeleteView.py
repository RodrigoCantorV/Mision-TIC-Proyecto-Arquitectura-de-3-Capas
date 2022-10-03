from rest_framework import views, status
from rest_framework.response import Response
from authApp.serializers.liquidacion_sueldoSerializer import Liquidacion_SueldoSerializer
from authApp.models.liquidacion_sueldo import Liquidacion_Sueldo
from django.http import Http404

class Liquidacion_SueldoDeleteView(views.APIView):
    def get_object(self, pk):
        try:
            return Liquidacion_Sueldo.objects.get(pk=pk)
        except Liquidacion_Sueldo.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
           post = self.get_object(pk)
           serializer = Liquidacion_SueldoSerializer(post)  
           return Response(serializer.data)
 

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


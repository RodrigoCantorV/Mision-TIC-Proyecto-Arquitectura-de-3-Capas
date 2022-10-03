from rest_framework import views, status
from rest_framework.response import Response
from authApp.serializers.liquidacion_sueldoSerializer import Liquidacion_SueldoSerializer
from authApp.models.liquidacion_sueldo import Liquidacion_Sueldo

class liquidacion_SueldoReadView(views.APIView):
    def get(self,request):
          # checking for the parameters from the URL
        items = Liquidacion_Sueldo.objects.all()
        serializer = Liquidacion_SueldoSerializer(items, many=True)

        # if there is something in items else raise error
        if items:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

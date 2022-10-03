from rest_framework import views, status
from rest_framework import serializers
from rest_framework.response import Response
from authApp.serializers.empleadoSerializer import EmpleadoSerializer
from authApp.models.empleado import Empleado

class EmpleadoCreateView(views.APIView):
    def get(self,request):
          # checking for the parameters from the URL
        items = Empleado.objects.all()
        serializer = EmpleadoSerializer(items, many=True)

        # if there is something in items else raise error
        if items:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
         item = EmpleadoSerializer(data=request.data)
         # validating for already existing data
         if Empleado.objects.filter(**request.data).exists():
             raise serializers.ValidationError('This data already exists')
         if item.is_valid():
             item.save()
             return Response(item.data)
         else:
             return Response(status=status.HTTP_404_NOT_FOUND)


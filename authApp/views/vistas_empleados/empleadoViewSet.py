from rest_framework import viewsets
from rest_framework import permissions
from authApp.models.empleado import Empleado 
from authApp.serializers.empleadoSerializer import EmpleadoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.AllowAny]
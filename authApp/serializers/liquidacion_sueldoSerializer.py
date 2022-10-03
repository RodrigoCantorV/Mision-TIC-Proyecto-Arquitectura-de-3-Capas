from rest_framework import serializers
from authApp.models.liquidacion_sueldo import Liquidacion_Sueldo

class Liquidacion_SueldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Liquidacion_Sueldo
        fields = [
         'num_liquidacion',
         'codigo_empleado',
         'fecha_liquidacion',
         'dias_laborados', 
         'sueldo',
         ]
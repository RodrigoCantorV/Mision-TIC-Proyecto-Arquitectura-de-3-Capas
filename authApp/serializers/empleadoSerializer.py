from rest_framework import serializers
from authApp.models.empleado import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = [
         'codio_empleado',
         ]

"""
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = [
         'codio_empleado',
         'cc_persona',
         'forma_pago',
         'numero_cuenta',
         'cesantias',
         'pension',
         'salud',
         'arl',
         'porcentaje_arl',
         'caja_compensacion',
         'centro_costos',
         'fecha_ingreso',
         'salario',
         'tipo_salario',
         'tipo_empleado',
         'tipo_contrato',
         'fin_contrato',
         'profesion',
         'oficio',
         'turno',
         'horas',
         'hora_entrada',
         'hora_salida',
         'inicio_vacaciones',
         'fin_vacaciones',
         'estado',
         
         ]
         """
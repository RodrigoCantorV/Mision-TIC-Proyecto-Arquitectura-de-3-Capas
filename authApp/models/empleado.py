from django.db import models
from .persona import Persona


class Empleado(models.Model):
    codio_empleado = models.IntegerField(primary_key=True)
    cc_persona = models.ForeignKey(Persona, related_name="Persona", blank=False, null=False, on_delete=models.CASCADE)  
    forma_pago = models.CharField(max_length= 80)
    numero_cuenta = models.CharField(max_length= 80)
    cesantias = models.CharField(max_length= 80)
    pension = models.CharField(max_length= 80)
    salud = models.CharField(max_length= 80)
    arl = models.CharField(max_length= 80)
    porcentaje_arl = models.CharField(max_length= 80)
    caja_compensacion = models.CharField(max_length= 80)
    centro_costos = models.CharField(max_length= 80)
    fecha_ingreso = models.DateField()
    salario = models.DecimalField(max_digits = 7, decimal_places = 0)
    tipo_salario = models.CharField(max_length= 80)
    tipo_empleado = models.CharField(max_length= 80)
    tipo_contrato = models.CharField(max_length= 80)
    fin_contrato = models.CharField(max_length= 80)
    profesion = models.CharField(max_length= 80)
    oficio = models.CharField(max_length= 80)
    turno = models.CharField(max_length= 80)
    horas =  models.IntegerField()
    hora_entrada = models.CharField(max_length= 80)
    hora_salida = models.CharField(max_length= 80)
    inicio_vacaciones = models.DateField()
    fin_vacaciones = models.DateField()
    estado = models.CharField(max_length= 80)
        
    
from django.db import models
from .empleado import Empleado

class Liquidacion_Sueldo(models.Model):
    num_liquidacion = models.IntegerField(primary_key=True)
    codigo_empleado = models.ForeignKey(Empleado, related_name="Empleado", blank=False, null=False, on_delete=models.CASCADE)  
    fecha_liquidacion = models.DateField()
    dias_laborados = models.IntegerField()
    sueldo = models.DecimalField(max_digits = 7, decimal_places = 0)
    #IBC = models.DecimalField(max_digits = 7, decimal_places = 0)
    #neto_pagar = models.DecimalField(max_digits = 7, decimal_places = 0)



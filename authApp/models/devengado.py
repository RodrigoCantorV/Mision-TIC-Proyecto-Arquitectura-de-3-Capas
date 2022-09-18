from django.db import models
from .liquidacion_sueldo import Liquidacion_Sueldo

class Devengado(models.Model):
    id_devengado = models.IntegerField(primary_key=True)
    codigo_liquidacion = models.ForeignKey(Liquidacion_Sueldo, related_name="Liquidacion", blank=False, null=False, on_delete=models.CASCADE)
    auxilio_trandporte = models.CharField(max_length=80)
    total_devengado = models.DecimalField(max_digits = 7, decimal_places = 0)
    
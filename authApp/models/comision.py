from django.db import models

class Comision(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80)
    sigla = models.CharField(max_length=80)
    recargo = models.DecimalField(max_digits = 7, decimal_places = 0)
    factor = models.IntegerField()
    
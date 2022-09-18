from django.db import models

class FSP(models.Model):
    id = models.IntegerField(primary_key=True)
    rengo = models.DecimalField(max_digits = 7, decimal_places = 0)
    porcentaje = models.IntegerField()

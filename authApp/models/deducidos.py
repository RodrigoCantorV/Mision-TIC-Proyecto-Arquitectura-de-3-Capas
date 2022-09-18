from django.db import models

class Deducidos(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.DecimalField(max_digits = 7, decimal_places = 0)

    
from django.db import models

# Create your models here.
""""
class Book(models.Model):
    id = models.IntegerField(max_length=100, primary_key=True)
    nombre = models.TextField(max_length= 80)
    autor = models.CharField(max_length= 80)
    precio = models.IntegerField(max_length= 80)        
"""
"""
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length= 80)
    autor = models.CharField(max_length= 80)
    precio = models.IntegerField()   
"""
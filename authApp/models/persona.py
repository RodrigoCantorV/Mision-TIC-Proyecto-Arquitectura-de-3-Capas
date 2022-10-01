import email
from django.db import models

# Create your models here.

class Persona(models.Model): 
    cc = models.IntegerField(primary_key=True)
    nombre1 = models.CharField(max_length= 80)
    #nombre2 = models.CharField(max_length= 80)
    apellido1 = models.CharField(max_length= 80)
    #apellido2 = models.CharField(max_length= 80)
    fecha = models.DateField(auto_now_add=True)
    #fecha = models.DateTimeField(auto_now_add=True)
    #direccion = models.CharField(max_length= 80)
    correo = models.EmailField(max_length= 80)
    #telefono = models.CharField(max_length= 80)
    celular = models.CharField(max_length= 80)
    #foto = models.CharField(max_length= 80)
    #estado_civil = models.CharField(max_length= 80)
    #tipo_sangre = models.CharField(max_length= 80)
    #genero = models.CharField(max_length= 80)
    #descripcion = models.TextField(max_length= 80)
    #libro = models.ForeignKey(Book, related_name="libros", blank=True, null=True, on_delete=models.CASCADE)

"""
##Define como se ve en el panel de administrador
    def __str__(self):
        cadena =  str(self.cc) + " "+self.nombre+ " "+self.apellido+ " "+  str(self.fecha)+" "+  str(self.email)+ " "+  str(self.libro)
        return cadena
"""


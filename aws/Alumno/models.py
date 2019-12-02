from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    edad = models.CharField(max_length=254, null=False)
    direccion = models.CharField(max_length=254, null=False)
    sexo = models.CharField(max_length=254, null=False)
    apellidoPaterno= models.CharField(max_length=254, null=False)
    apellidoMaterno= models.CharField(max_length=254, null=False)
    carrera = models.CharField(max_length=254, null=False)
    
    

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Alumno'
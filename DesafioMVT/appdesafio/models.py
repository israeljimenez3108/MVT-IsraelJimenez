from django.db import models

# Create your models here.

#Creamos la clase Familia para utilizarla como tabla en la db

class Familia(models.Model):

    nombre = models.CharField(max_length=70)
    fecha_nac = models.DateField()
    edad = models.IntegerField()

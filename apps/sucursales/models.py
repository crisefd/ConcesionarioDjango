from django.db import models 
from django.conf import settings



class Sucursales(models.Model):
	nombre = models.CharField(max_length=50, default='')
	direccion = models.CharField(max_length=30, default='')
	#ganancias = FloatField()

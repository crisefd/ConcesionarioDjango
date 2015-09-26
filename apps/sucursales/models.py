from django.db.models import * 
from django.conf import settings



class Sucursales(Model):
	nombre = CharField(max_length=50, default='')
	direccion = CharField(max_length=30, default='')
	#ganancias = FloatField()

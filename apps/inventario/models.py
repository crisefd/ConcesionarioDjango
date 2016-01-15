from django.db import models
from django.conf import settings


class Item_Inventario(models.Model):
    precio = models.FloatField(default=0.0)
    cantidad = models.IntegerField(default=1)
    marca = models.CharField(max_length=50, default='')
    class Meta:
        abstract = True


class Automovil(Item_Inventario):
    modelo = models.CharField(max_length=50, default='')
    def __unicode__(self):
        return "%s %s " % (self.marca, self.modelo)

class Repuesto(Item_Inventario):
    nombre = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return "%s %s " % (self.nombre, self.marca)
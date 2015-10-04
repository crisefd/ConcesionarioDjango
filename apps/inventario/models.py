from django.db import models
from django.conf import settings


class Item_Inventario(models.Model):
    serial_id = models.CharField(max_length=50, primary_key=True,
                            default = '0000')
    precio = models.FloatField(default=0.0)
    disponible = models.BooleanField(default=True)


    class Meta:
        abstract = True


class Automovil(Item_Inventario):
    marca = models.CharField(max_length=50, default='Acme')
    modelo = models.CharField(max_length=50, default='Acme')

    def __unicode__(self):
        return "%s %s %s" % (self.serial_id, self.marca, self.modelo)

class Repuesto(Item_Inventario):
    nombre = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return "%s %s" % (self.serial_id, self.nombre)
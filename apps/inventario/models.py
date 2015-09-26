from django.db import models
from django.conf import settings


class Item_Inventario(Model):
    serial_id = CharField(max_length=50, primary_key=True,
                            default = '0000')
    precio = FloatField(default=0.0)

    class Meta:
        abstract = True


class Automovil(Item_Inventario):
    marca = CharField(max_length=50, default='Acme')
    modelo = CharField(max_length=50, default='Acme')

class Repuesto(Item_Inventario):
    nombre = CharField(max_length=50, default='')
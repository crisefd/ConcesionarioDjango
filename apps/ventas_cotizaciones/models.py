from django.db import models
from django.conf import settings


# Create your models here.
class Ventas(Model):
    vendedor_fk = ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = CharField(max_length=50, default='')
    doc_id_comprador = CharField(max_length=50, unique=True, default='00000000')
    automovil_fk = ForeignKey(Automovil, null=True)
    valor_venta = FloatField(default=0.0)


class Cotizaciones(Model):
    automovil_fk = ForeignKey(settings.MODELO_AUTO)
    vendedor_fk = ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = CharField(max_length=50, default='')
    #valor = FloatField(null=False)

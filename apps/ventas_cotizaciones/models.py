from django.db import models
from django.conf import settings


# Create your models here.
class Ventas(models.Model):
    vendedor_fk = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = models.CharField(max_length=50, default='')
    doc_id_comprador = models.CharField(max_length=50, unique=True, default='00000000')
    automovil_fk = models.ForeignKey(settings.MODELO_AUTO, null=True)
    valor_venta = models.FloatField(default=0.0)


class Cotizaciones(models.Model):
    automovil_fk = models.ForeignKey(settings.MODELO_AUTO)
    vendedor_fk = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = models.CharField(max_length=50, default='')
    #valor = FloatField(null=False)

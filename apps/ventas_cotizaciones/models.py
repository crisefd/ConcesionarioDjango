from django.db import models
from django.conf import settings
from django.utils import timezone


class Ventas(models.Model):
    vendedor_fk = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = models.CharField(max_length=50, default='')
    doc_id_comprador = models.CharField(max_length=50, unique=True,
                                    default='00000000')
    automovil_fk = models.ForeignKey(settings.MODELO_AUTO, null=True)
    valor_venta = models.FloatField(default=0.0)
    fecha = models.DateField(default=timezone.now)


class Cotizaciones(models.Model):
    automovil_fk = models.ForeignKey(settings.MODELO_AUTO)
    vendedor_fk = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = models.CharField(max_length=50, default='')
    fecha = models.DateField(default=timezone.now)
    #valor = FloatField(null=False)

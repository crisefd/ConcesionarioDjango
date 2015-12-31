from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.inventario.models import Automovil

class Cotizaciones(models.Model):
    automovil = models.ForeignKey(settings.MODELO_AUTO)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre_comprador = models.CharField(max_length=50, default='')
    fecha = models.DateField(default=timezone.now)

class Ventas(models.Model):
    automovil = models.ForeignKey(settings.MODELO_AUTO)
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL)
    sucursal = models.ForeignKey(settings.MODELO_SUCURSALES, default='')
    nombre_comprador = models.CharField(max_length=50, default='')
    doc_id_comprador = models.CharField(max_length=50,default='')
    valor_venta = models.FloatField(default=0.0)
    fecha = models.DateField(default=timezone.now)


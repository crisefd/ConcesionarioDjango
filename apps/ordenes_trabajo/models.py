from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Mecanicos(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return "%s %s" % (self.nombre, self.apellido)


class Ordenes_Trabajo(models.Model):
    ACTIVA = "Activa"
    CANCELADA = "Cancelada"
    FINALIZADA = "Finalizada"
    ESTADOS = ((ACTIVA,"Activa"), (CANCELADA, "Cancelada"), (FINALIZADA, "Finalizada"),)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    mecanico_asignado = models.ForeignKey(Mecanicos)
    descripcion = models.TextField(max_length=350, null=True)
    matricula_vehiculo = models.CharField(max_length=10, null=True)
    jefe_taller = models.ForeignKey(settings.AUTH_USER_MODEL)
    costo = models.FloatField(default=500)
    estado = models.CharField(max_length=50, choices=ESTADOS, default=ACTIVA)

    def __unicode__(self):
        return "orden %d " % self.id


class Orden_Repuesto(models.Model):
    orden = models.ForeignKey(Ordenes_Trabajo)
    repuesto = models.ForeignKey(settings.MODELO_REPUESTO)
    fecha = models.DateTimeField(default=timezone.now)



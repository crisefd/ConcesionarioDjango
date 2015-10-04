from django.db import models
from django.conf import settings

# Create your models here.
class Mecanicos(models.Model):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return "%s %s" % (self.nombre, self.apellido)


class Ordenes_Trabajo(models.Model):
    ACTIVA = "ACTIVA"
    CANCELADA = "CANCELADA"
    FINALIZADA = "FINALIZADA"
    ESTADOS = ((ACTIVA,"Activa"), (CANCELADA, "Cancelada"), (FINALIZADA, "Finalizada"),)
    timestamp = models.DateTimeField(auto_now=True)
    mecanico_asignado = models.ForeignKey(Mecanicos)
    descripcion = models.TextField(max_length=350, null=True)
    matricula_vehiculo = models.CharField(max_length=10, unique=True, null=True)
    jefe_taller_fk = models.ForeignKey(settings.AUTH_USER_MODEL)
    estado = models.CharField(max_length=50, choices=ESTADOS, default=ACTIVA)

    def __unicode__(self):
        return "orden %d " % self.id
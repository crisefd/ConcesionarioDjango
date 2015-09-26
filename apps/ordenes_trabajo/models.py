from django.db import models
from django.conf import settings

# Create your models here.
class Mecanicos(Model):
    nombre = CharField(max_length=50, default='')
    apellido = CharField(max_length=50, default='')


class Ordenes_Trabajo(Model):
    ACTIVA = "Activa"
    CANCELADA = "CANCELADA"
    FINALIZADA = "FINALIZADA"
    ESTADOS = ((ACTIVA,"Activa"), (CANCELADA, "Cancelada"), (FINALIZADA, "Finalizada"),)
    mecanico_asignado = ForeignKey(Mecanicos)
    descripcion = CharField(max_length=150, null=True)
    matricula_vehiculo = CharField(max_length=10, unique=True, null=True)
    jefe_taller_fk = ForeignKey(settings.AUTH_USER_MODEL)
    estado = CharField(max_length=50, choices=ESTADOS, default=ACTIVA)
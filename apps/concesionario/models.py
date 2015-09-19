from django.db.models import * 
from django.conf import settings



class Sucursales(Model):
	nombre = CharField(max_length=50, default='')
	direccion = CharField(max_length=30, default='')
	#ganancias = FloatField()


class Mecanicos(Model):
	nombre = CharField(max_length=50, default='')
	apellido = CharField(max_length=50, default='')

class Item_Inventario(Model):
	serial_id = CharField(max_length=50, primary_key=True, default = '0000')
	precio = FloatField(default=0.0)

	class Meta:
		abstract = True


class Automovil(Item_Inventario):
	marca = CharField(max_length=50, default='Acme')
	modelo = CharField(max_length=50, default='Acme')

class Repuesto(Item_Inventario):
	nombre = CharField(max_length=50, default='')


class Ventas(Model):
	vendedor_fk = ForeignKey(settings.AUTH_USER_MODEL)
	nombre_comprador = CharField(max_length=50, default='')
	doc_id_comprador = CharField(max_length=50, unique=True, default='00000000')
	automovil_fk = ForeignKey(Automovil, null=True)
	valor_venta = FloatField(default=0.0)


class Cotizaciones(Model):
	automovil_fk = ForeignKey(Automovil)
	vendedor_fk = ForeignKey(settings.AUTH_USER_MODEL)
	nombre_comprador = CharField(max_length=50, default='')
	#valor = FloatField(null=False)


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
from django.db.models import * 
from django.conf import settings



class Sucursales(Model):
	nombre = CharField(max_length=50, null=True)
	direccion = CharField(max_length=30, null=True)
	#ganancias = FloatField()


class Mecanicos(Model):
	nombre = CharField(max_length=50, null=True)
	apellido = CharField(max_length=50, null=True)

class Item_Inventario(Model):
	serial_id = CharField(max_length=50, primary_key=True, default = '0000')
	precio = FloatField(null=True)

	class Meta:
		abstract = True


class Automovil(Item_Inventario):
	marca = CharField(max_length=50, null=True)
	modelo = CharField(max_length=50, null=True)

class Repuesto(Item_Inventario):
	nombre = CharField(max_length=50, null=True)


class Ventas(Model):
	vendedor_fk = ForeignKey(settings.MODELO_AUT_VENDEDOR)
	nombre_comprador = CharField(max_length=50, null=True)
	doc_id_comprador = CharField(max_length=50, unique=True, null=True)
	automovil_fk = ForeignKey(Automovil, null=True)
	valor_venta = FloatField(null=True)


class Cotizaciones(Model):
	automovil_fk = ForeignKey(Automovil)
	vendedor_fk = ForeignKey(settings.MODELO_AUT_VENDEDOR)
	nombre_comprador = CharField(max_length=50, null=True)
	#valor = FloatField(null=False)


class Ordenes_Trabajo(Model):
	ACTIVA = "Activa"
	CANCELADA = "CANCELADA"
	FINALIZADA = "FINALIZADA"
	ESTADOS = ((ACTIVA,"Activa"), (CANCELADA, "Cancelada"), (FINALIZADA, "Finalizada"),)
	mecanico_asignado = ForeignKey(Mecanicos)
	descripcion = CharField(max_length=150, null=True)
	matricula_vehiculo = CharField(max_length=10, unique=True, null=True)
	jefe_taller_fk = ForeignKey(settings.MODELO_AUT_JEFE)
	estado = CharField(max_length=50, choices=ESTADOS, default=ACTIVA)
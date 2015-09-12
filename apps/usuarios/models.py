from django.db.models import *
from django.conf import settings
from django.contrib.auth.models import *


"""
class UserManager(BaseUserManager, Manager):
	def _create_user(self, username, email, password, is_staff,
					is_superuser, **extra_fields):
		if not email:
			raise ValueError("El email es obligatorio")
		email = self.normalize_email(email)
		user_ = self.model(username=username, email=email, is_active=True,
							is_staff=is_staff, is_superuser=is_superuser, **extra_fields)

		user_.set_password(password)
		user_.save(using=self._db)
		return user_

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False,
				False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True,
				True, **extra_fields)
"""

#class User():
class Persona(Model):
	nombre = CharField(max_length=50, null=True)
	apellido = CharField(max_length=50, null=True)
	passwd = CharField(max_length=30, null=True)
	fecha_nacimiento = DateField(null=True)
	genero = CharField(max_length=1, null=True)
	correo_electronico = EmailField(unique=True, null=True)
	numero_telefono = CharField(max_length=50, unique=True, null=True)
	direccion_residencia = CharField(max_length=50, unique=True, null=True)
	documento_id = CharField(max_length=30, primary_key=True, blank=True)
	esta_activo = BooleanField(default=True)
	#objects = UserManager()

	class Meta:
		abstract = True


class Gerente(Persona):
	pass


class Vendedor(Persona):
	sucursal_fk = ForeignKey(settings.MODELO_SUCURSALES)
	num_ventas = PositiveIntegerField(default=0)


class Jefe_Taller(Persona):
	sucursal_fk = ForeignKey(settings.MODELO_SUCURSALES)
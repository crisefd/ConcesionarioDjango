from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import *
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.signals import user_logged_in

def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
user_logged_in.connect(update_last_login)


class PermissionManager(Manager):
    use_in_migrations = True

    def get_by_natural_key(self, codename, app_label, model):
        return self.get(
            codename=codename,
            content_type=ContentType.objects.db_manager(self.db).get_by_natural_key(app_label, model),
        )


@python_2_unicode_compatible
class Permission_(Model):
    """
    The permissions system provides a way to assign permissions to specific
    users and groups of users.
    The permission system is used by the Django admin site, but may also be
    useful in your own code. The Django admin site uses permissions as follows:
        - The "add" permission limits the user's ability to view the "add" form
          and add an object.
        - The "change" permission limits a user's ability to view the change
          list, view the "change" form and change an object.
        - The "delete" permission limits the ability to delete an object.
    Permissions are set globally per type of object, not per specific object
    instance. It is possible to say "Mary may change news stories," but it's
    not currently possible to say "Mary may change news stories, but only the
    ones she created herself" or "Mary may only change news stories that have a
    certain status or publication date."
    Three basic permissions -- add, change and delete -- are automatically
    created for each Django model.
    """
    name = CharField(_('name'), max_length=255)
    content_type =ForeignKey(
        ContentType,
        CASCADE,
        verbose_name=_('content type'),
    )
    codename =CharField(_('codename'), max_length=100)
    objects = PermissionManager()

    class Meta:
        verbose_name = _('permission')
        verbose_name_plural = _('permissions')
        unique_together = (('content_type', 'codename'),)
        ordering = ('content_type__app_label', 'content_type__model',
                    'codename')

    def __str__(self):
        return "%s | %s | %s" % (
            six.text_type(self.content_type.app_label),
            six.text_type(self.content_type),
            six.text_type(self.name))

    def natural_key(self):
        return (self.codename,) + self.content_type.natural_key()
    natural_key.dependencies = ['contenttypes.contenttype']


class GroupManager(Manager):
    """
    The manager for the auth's Group model.
    """
    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


@python_2_unicode_compatible
class Group(Model):
    """
    Groups are a generic way of categorizing users to apply permissions, or
    some other label, to those users. A user can belong to any number of
    groups.
    A user in a group automatically has all the permissions granted to that
    group. For example, if the group Site editors has the permission
    can_edit_home_page, any user in that group will have that permission.
    Beyond permissions, groups are a convenient way to categorize users to
    apply some label, or extended functionality, to them. For example, you
    could create a group 'Special users', and you could write code that would
    do special things to those users -- such as giving them access to a
    members-only portion of your site, or sending them members-only email
    messages.
    """
    name = CharField(_('name'), max_length=80, unique=True)
    permissions = ManyToManyField(
        Permission_,
        verbose_name=('permissions'),
        blank=True,
    )

    objects = GroupManager()

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)


class PermissionsMixin(Model):
    """
    A mixin class that adds the fields and methods necessary to support
    Django's Group and Permission model using the ModelBackend.
    """
    is_superuser = BooleanField(
        _('superuser status'),
        default=False,
        help_text=(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )
    groups = ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )
    user_permissions = ManyToManyField(
        Permission_,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    class Meta:
        abstract = True

    def get_group_permissions(self, obj=None):
        """
        Returns a list of permission strings that this user has through their
        groups. This method queries all available auth backends. If an object
        is passed in, only permissions matching this object are returned.
        """
        permissions = set()
        for backend in auth.get_backends():
            if hasattr(backend, "get_group_permissions"):
                permissions.update(backend.get_group_permissions(self, obj))
        return permissions

    def get_all_permissions(self, obj=None):
        return _user_get_all_permissions(self, obj)

    def has_perm(self, perm, obj=None):
        """
        Returns True if the user has the specified permission. This method
        queries all available auth backends, but returns immediately if any
        backend returns True. Thus, a user who has permission from a single
        auth backend is assumed to have permission in general. If an object is
        provided, permissions for this specific object are checked.
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        """
        Returns True if the user has each of the specified permissions. If
        object is passed, it checks if the user has all required perms for this
        object.
        """
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        """
        Returns True if the user has any permissions in the given app label.
        Uses pretty much the same logic as has_perm, above.
        """
        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

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



#class AbstractUser(AbstractBaseUser, PermissionsMixin):
class User(AbstractBaseUser, PermissionsMixin):
	nombre = CharField(max_length=50, blank=True)
	apellido = CharField(max_length=50, blank=True)
	passwd = CharField(max_length=30, blank=True)
	fecha_nacimiento = DateField(blank=True)
	genero = CharField(max_length=1, blank=True)
	correo_electronico = EmailField(unique=True, blank=True)
	numero_telefono = CharField(max_length=50, unique=True, blank=True)
	direccion_residencia = CharField(max_length=50, unique=True, blank=True)
	documento_id = CharField(max_length=30, primary_key=True, blank=True)
	esta_activo = BooleanField(default=True)
	tipo = CharField(max_length=50)
	objects = UserManager()

	USERNAME_FIELD = _('correo_electronico')
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')


#class User(AbstractUser):
	#class Meta(AbstractUser.Meta):
	#	swappable = 'AUTH_USER_MODEL'



class Vendedor_Sucursal(Model):
	sucursal_fk = ForeignKey(settings.MODELO_SUCURSALES)
	vendedor_fk = ForeignKey(User)


class JefeTaller_Sucursal(Model):
	sucursal_fk = ForeignKey(settings.MODELO_SUCURSALES)
	jefe_fk = ForeignKey(User)


"""
class Gerente(Persona):
	pass


class Vendedor(Persona):
	sucursal_fk = ForeignKey(settings.MODELO_SUCURSALES)
	num_ventas = PositiveIntegerField(default=0)


class Jefe_Taller(Persona):
	sucursal_fk = ForeignKey(settings.MODELO_SUCURSALES)"""
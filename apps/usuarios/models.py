
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        if not email:
            raise ValueError('The given email must be set')        
        #is_active = extra_fields.pop("is_active", True)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        print "CAMPOS EXTRAS", extra_fields
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)



class AbstractUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, unique=True, default='examplename')
    email= models.EmailField(_('email address'),max_length=50, unique=True,)
    is_staff = models.BooleanField(('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    birth_date = models.DateField(default='1930-01-01')
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    id_document = models.CharField(max_length=50, primary_key=True, blank=True)
    objects = UserManager()
    charge = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    branch = models.ForeignKey(settings.MODELO_SUCURSALES, null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True



class User(AbstractUser):

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


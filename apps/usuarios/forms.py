from django.forms import Form
from django.forms import ModelForm
from usuario.models import *


class GerenteForm(ModelForm):
    nombre = forms.CharField(max_length= 50)
    apellido= forms.CharField(max_length=50)
    passwd = forms.CharFiel(max_length=50)
    fecha_nacimiento = forms.DateField()
    genero = forms.CharField(max_length=50)
    correo_electronico = forms.EmailField(max_length=100)
    numero_telefono = forms.CharField(max_length=50)
    direccion_residencia = forms.CharField(max_length=50)
    documento_id = forms.CharField(max_length=50)
    esta_activo= forms.BooleanFiel(default=True)

    class Meta:
        model = Gerente


class Jefe_TallerForm(ModelForm):
    nombre = forms.CharField(max_length= 50)
    apellido= forms.CharField(max_length=50)
    passwd = forms.CharFiel(max_length=50)
    fecha_nacimiento = forms.DateField()
    genero = forms.CharField(max_length=50)
    correo_electronico = forms.EmailField(max_length=100)
    numero_telefono = forms.CharField(max_length=50)
    direccion_residencia = forms.CharField(max_length=50)
    documento_id = forms.CharField(max_length=50)
    esta_activo= forms.BooleanFiel(default=True)
    sucursal = forms.CharField(max_length=50)

    class Meta:
        model = Jefe_Taller

    

class VendedorForm(ModelForm):
    nombre = forms.CharField(max_length= 50)
    apellido= forms.CharField(max_length=50)
    passwd = forms.CharFiel(max_length=50)
    fecha_nacimiento = forms.DateField()
    genero = forms.CharField(max_length=50)
    correo_electronico = forms.EmailField(max_length=100)
    numero_telefono = forms.CharField(max_length=50)
    direccion_residencia = forms.CharField(max_length=50)
    documento_id = forms.CharField(max_length=50)
    esta_activo= forms.BooleanFiel(default=True)
    num_ventas= forms.PositiveIntgerField()
    sucursal = forms.CharField(max_length=50)

    class Meta:
        model = Vendedor


    
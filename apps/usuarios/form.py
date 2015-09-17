from django import forms
from django.forms import ModelForm
from usuario.models import Persona

class Persona(forms.Form):
    nombre = forms.CharField(max_length= 50)
    apellido= forms.CharField(max_length=50)
    passwd = forms.CharFiel(max_length=50)
    fecha_nacimiento = forms.DateField()
    genero = forms.CharField(max_length=50)
    correo_electronico = forms.EmailField(max_length=100)
    numero_telefono = forms.CharField(max_length=50)
    direccion_residencia = forms.CharField(max_length=50)
    documento_id = forms.CharField(max_length=50)
    esta_activo= forms.BooleanFiel(default=true)
    
class NewPersona(ModelForm):
    
    
    
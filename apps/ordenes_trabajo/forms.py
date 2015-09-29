from django import forms
#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *

class Ordenes_TrabajoForm(forms.ModelForm):
    class Meta:
        model = Ordenes_Trabajo
        fields = ('mecanico_asignado', 'descripcion', 
            'matricula_vehiculo', 'jefe_taller_fk', 'estado')

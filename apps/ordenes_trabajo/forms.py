from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *

class Ordenes_TrabajoForm(forms.ModelForm):
    mecanico_asignado = forms.ModelChoiceField(queryset=Mecanicos.objects.all())
    descripcion = forms.Textarea()
    class Meta:
        model = Ordenes_Trabajo
        fields = ('mecanico_asignado', 'descripcion', 
            'matricula_vehiculo', 'jefe_taller_fk', 'estado')

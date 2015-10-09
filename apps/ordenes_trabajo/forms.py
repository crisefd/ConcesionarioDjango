from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from apps.usuarios.models import User
from .models import *

class Ordenes_TrabajoForm(forms.ModelForm):
    mecanico_asignado = forms.ModelChoiceField(queryset=Mecanicos.objects.all())
    jefe_taller = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Jefe Taller"))
    descripcion = forms.Textarea()
    class Meta:
        model = Ordenes_Trabajo
        fields = ('mecanico_asignado', 'descripcion', 
            'matricula_vehiculo', 'jefe_taller', 'estado')

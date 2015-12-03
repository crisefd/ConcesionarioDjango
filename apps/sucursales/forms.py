from django import forms
from django.forms import ModelForm
from .models import *

class SucursalesForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)

    class Meta:
        model = Sucursales
        fields = ('nombre', 'direccion')
    

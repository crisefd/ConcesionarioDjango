from django import forms
#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *


class AutomovilForm(forms.ModelForm):
    precio = forms.FloatField(min_value=1.0)
    class Meta:
        model = Automovil
        fields = ('precio', 'marca', 'modelo', 'cantidad')


class RepuestoForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1)
    precio = forms.FloatField(min_value=1.0)
    class Meta:
        model = Repuesto
        fields = ('precio', 'nombre','marca', 'cantidad')
    
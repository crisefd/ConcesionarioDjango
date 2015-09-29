from django import forms
#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *


class AutomovilForm(forms.ModelForm):
    class Meta:
        model = Automovil
        fields = ('serial_id', 'precio', 'marca', 'modelo')


class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ('serial_id', 'precio', 'nombre')
    
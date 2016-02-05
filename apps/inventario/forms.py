from django import forms
#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *


class AutomovilForm(forms.ModelForm):
    precio = forms.FloatField(min_value=1.0,widget=forms.NumberInput(attrs={
    	'class':'form-control'
    	}))
    marca=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'MarcaInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    modelo=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'ModelInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    cantidad = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={
    	'class':'form-control',
    	'defaultValue':'1'
    	}))
    class Meta:
        model = Automovil
        fields = ('precio', 'marca', 'modelo', 'cantidad')


class RepuestoForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1,widget=forms.NumberInput(attrs={
    	'class':'form-control'
    	}))
    precio = forms.FloatField(min_value=1.0,widget=forms.NumberInput(attrs={
    	'class':'form-control'
    	}))
    marca=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'MarcaInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    nombre=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'NameInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    class Meta:
        model = Repuesto
        fields = ('precio', 'nombre','marca', 'cantidad')
    
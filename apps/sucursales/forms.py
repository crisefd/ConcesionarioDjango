from django import forms
from django.forms import ModelForm
from .models import *

class SucursalesForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'ModelInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    direccion = forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'ModelInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))

    class Meta:
        model = Sucursales
        fields = ('nombre', 'direccion')
    

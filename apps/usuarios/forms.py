from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50,
            widget = forms.TextInput(attrs = {
                    'type' : 'password'
                }))



class MyUserCreationForm(UserCreationForm):
    sex = forms.ChoiceField(choices=[("masculino", "M"),
        ("femenimo", "F"),], widget=forms.RadioSelect())

    YEARS = [y for y in range(1930,2015)]
    birth_date = forms.DateField(widget=SelectDateWidget(years=YEARS))
    charge = forms.ChoiceField(choices=[("Gerente","Gerente"),
                                ("Vendedor", "Vendedor"), ("Jefe Taller", "Jefe Taller")],
                                    widget= forms.RadioSelect())
    phone_number = forms.CharField(max_length = 50)
    id_document = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 255)


class JefeTallerSucursalForm(ModelForm):
    class Meta:
        model = JefeTaller_Sucursal
        fields = ['sucursal_fk', 'jefe_fk']

class VendedorSucursalForm(ModelForm):
    class Meta:
        model = Vendedor_Sucursal
        fields = ['sucursal_fk', 'vendedor_fk']

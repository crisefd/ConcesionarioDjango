from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *
from apps.sucursales.models import Sucursales

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50)
    password = forms.CharField(max_length = 50,
            widget = forms.TextInput(attrs = {
                    'type' : 'password'
                }))



class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    sex = forms.ChoiceField(choices=[("M", "M"),
        ("F", "F"),], widget=forms.RadioSelect())

    YEARS = [y for y in range(1930,2015)]
    birth_date = forms.DateField(widget=SelectDateWidget(years=YEARS,
                                                        attrs={'class':'fecha'}))
    charge = forms.ChoiceField(choices=[("Gerente","Gerente"),
                                ("Vendedor", "Vendedor"), ("Jefe Taller", "Jefe Taller")],
                                    widget= forms.RadioSelect())
    phone_number = forms.CharField(max_length = 50)
    id_document = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 255)
    address = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    branch = forms.ModelChoiceField(queryset=Sucursales.objects.all())
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name","last_name","username", "email","address", "phone_number", 
            "id_document","sex", "charge", "birth_date", "branch")

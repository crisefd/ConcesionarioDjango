from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *
from apps.sucursales.models import Sucursales
from apps.usuarios.models import User
from django.contrib.auth.forms import AdminPasswordChangeForm

class LoginForm(forms.Form):


    username = forms.CharField(max_length = 50,
            widget=forms.TextInput(attrs ={
                    'id':'usernameInput'
                }))
    password = forms.CharField(max_length = 50,
            widget = forms.TextInput(attrs = {
                    'type' : 'password',
                    'id':'passwordInput'
                }))




class EditProfileForm(forms.Form):
    phone_number = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)

    def set_fields(self, username):
        self.user = User.objects.get(username=username)
        self.fields['phone_number'].initial = self.user.phone_number
        self.fields['address'].initial = self.user.address
        self.fields['email'].initial = self.user.email

    def update(self):
        print "SALVADO!"
        #user = super(EditProfileForm, self).save(commit=False)
        self.user.phone_number = self.cleaned_data['phone_number']
        self.user.address = self.cleaned_data['address']
        self.user.email = self.cleaned_data['email']
        self.user.save()


    class Meta:
        model = User


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
    phone_number = forms.CharField(max_length = 50, 
                                  widget = forms.TextInput(attrs={
                                                        'id':'telephoneInput',
                                                        'type':'text'
                                                        
                                   }))
    id_document = forms.CharField(max_length = 50)
    email = forms.EmailField(max_length = 255,
                              widget = forms.TextInput(attrs={
                                                       'id':'emailInput'
                                }))
    address = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    branch = forms.ModelChoiceField(queryset=Sucursales.objects.all())

    def save(self, commit=True):
        if self.cleaned_data['charge'] == "Gerente":
            self.cleaned_data['branch'] = ''
        return super(MyUserCreationForm, self).save(commit)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name","last_name","username", "email","address", "phone_number", 
            "id_document","sex", "charge", "birth_date", "branch")

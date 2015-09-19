from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget

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
    birthdate = forms.DateField(widget=SelectDateWidget(years=YEARS))

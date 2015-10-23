from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from apps.usuarios.models import User
from apps.inventario.models import Repuesto
from .models import *

class Ordenes_TrabajoForm(forms.ModelForm):
    mecanico_asignado = forms.ModelChoiceField(queryset=Mecanicos.objects.all())
    jefe_taller = forms.ModelChoiceField(queryset=User.objects.all())
    #jefe_taller = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Jefe Taller"))
    #jefe_taller = forms.ModelChoiceField(queryset=User.objects.filter(username='ironman'))
    descripcion = forms.Textarea()

    def set_jefe_taller(self, jefe_username):
        queryset = User.objects.filter(username=jefe_username)
        #print queryset
        self.fields['jefe_taller'].queryset = queryset

    class Meta:
        model = Ordenes_Trabajo
        #fields = ('mecanico_asignado', 'descripcion', 
         #   'matricula_vehiculo', 'jefe_taller', 'estado')
        exclude = ('costo', 'timestamp', 'estado')

class Orden_RepuestoForm(forms.ModelForm):
    orden = forms.ModelChoiceField(queryset=Ordenes_Trabajo.objects.filter(estado='Activa'))
    repuesto = forms.ModelChoiceField(queryset=Repuesto.objects.filter(disponible=True))

    def save(self, *args, **kwargs):
        pk_rep = self.cleaned_data['repuesto'].id
        pk_ord = self.cleaned_data['orden'].id
        ord_ = Ordenes_Trabajo.objects.get(pk=pk_ord)
        rep = Repuesto.objects.get(pk=pk_rep)
        rep.disponible = False
        ord_.costo = rep.precio
        rep.save()
        ord_.save()
        return super(Orden_RepuestoForm, self).save(*args, **kwargs)

    class Meta:
        model = Orden_Repuesto
        fields = ('orden', 'repuesto')

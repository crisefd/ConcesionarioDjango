from django import forms
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from .models import *

from apps.inventario.models import Automovil
from apps.usuarios.models import User

class VentasForm(forms.ModelForm):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.filter(disponible=True))
    vendedor = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Vendedor"))

    def save(self, *args, **kwargs):
        key = self.cleaned_data['automovil'].serial_id
        auto = Automovil.objects.get(pk=key)
        auto.disponible = False
        self.cleaned_data['valor_venta'] = self.cleaned_data['automovil'].precio
        auto.save()
        return super(VentasForm, self).save(*args, **kwargs)

    class Meta:
        model = Ventas
        fields = ('vendedor', 'nombre_comprador', 'doc_id_comprador',
                 'automovil')

class CotizacionesForm(forms.ModelForm):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.filter(disponible=True))
    vendedor = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Vendedor"))

    def save(self, *args, **kwargs):
        return super(CotizacionesForm, self).save(*args, **kwargs)
    
    class Meta:
        model = Cotizaciones
        fields = ('automovil', 'vendedor', 'nombre_comprador')

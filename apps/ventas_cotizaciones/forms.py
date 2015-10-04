from django import forms
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from .models import *

from apps.inventario.models import Automovil
from apps.usuarios.models import User

class VentasForm(forms.ModelForm):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.filter(disponible=True))
    vendedor = forms.ModelChoiceField(queryset=User.objects.all())

    def save(self, *args, **kwargs):
        key = self.cleaned_data['automovil'].serial_id
        auto = Automovil.objects.get(pk=key)
        auto.disponible = False
        auto.save()
        self.cleaned_data['valor_venta'] = self.cleaned_data['automovil'].precio
        return super(VentasForm, self).save(*args, **kwargs)

    class Meta:
        model = Ventas
        fields = ('vendedor', 'nombre_comprador', 'doc_id_comprador',
                 'automovil')

class CotizacionesForm(forms.ModelForm):
    automovil_fk = forms.ModelChoiceField(queryset=Automovil.objects.filter(disponible=True))
    vendedor_fk = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Cotizaciones
        fields = ('automovil', 'vendedor', 'nombre_comprador')

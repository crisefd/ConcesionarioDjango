from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *

class VentasForm(forms.ModelForm):
    automovil_fk = forms.ModelChoiceField(queryset=settings.MODELO_AUTO.objects.all())
    class Meta:
        model = Ventas
        fields = ('vendedor_fk', 'nombre_comprador', 'doc_id_comprador',
                 'automovil_fk', 'valor_venta')

class CotizacionesForm(forms.ModelForm):
    class Meta:
        model = Cotizaciones
        fields = ('automovil_fk', 'vendedor_fk', 'nombre_comprador')
    
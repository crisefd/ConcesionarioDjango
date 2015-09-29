from django import forms
#from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms.extras.widgets import SelectDateWidget
from .models import *

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ('vendedor_fk', 'nombre_comprador', 'doc_id_comprador',
                 'automovil_fk', 'valor_venta', 'fecha')

class CotizacionesForm(forms.ModelForm):
    class Meta:
        model = Cotizaciones
        fields = ('automovil_fk', 'vendedor_fk', 'nombre_comprador',
                'fecha')
    
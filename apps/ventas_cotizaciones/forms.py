from django import forms
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from apps.usuarios.models import User
from .models import *
from apps.inventario.models import Automovil
from apps.sucursales.models import Sucursales


class VentasForm(forms.ModelForm):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.filter(cantidad__gte = 1))
    #vendedor = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Vendedor"))
    #sucursal = forms.ModelChoiceField(queryset=Sucursales.objects.filter(is_active=True))
    def save(self, *args, **kwargs):
        pk = self.cleaned_data['automovil'].id
        auto = Automovil.objects.get(pk=pk)
        self.cleaned_data['valor_venta'] = self.cleaned_data['automovil'].precio
        auto.cantidad -= 1
        auto.save()
        return super(VentasForm, self).save(*args, **kwargs)

    def asignar_vendedor_sucursal(self, vendedor_username):
        queryset_vendedor = User.objects.filter(username=vendedor_username)
        queryset_sucursal = Sucursales.objects.filter(pk=queryset_vendedor[0].branch_id)
        self.fields['vendedor'].queryset = queryset_vendedor
        self.fields['sucursal'].queryset = queryset_sucursal

    class Meta:
        model = Ventas
        fields = ('vendedor', 'sucursal','nombre_comprador', 'doc_id_comprador',
                 'automovil')

class CotizacionesForm(forms.ModelForm):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.filter(cantidad__gte = 1))
    vendedor = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Vendedor"))

    def save(self, *args, **kwargs):
        return super(CotizacionesForm, self).save(*args, **kwargs)

    def set_vendedor(self, vendedor_username):
        queryset = User.objects.filter(username=vendedor_username)
        self.fields['vendedor'].queryset = queryset
    
    class Meta:
        model = Cotizaciones
        fields = ('automovil', 'vendedor', 'nombre_comprador')

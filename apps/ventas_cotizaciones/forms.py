from django import forms
from django.conf import settings
from django.forms.extras.widgets import SelectDateWidget
from apps.usuarios.models import User
from .models import *
from apps.inventario.models import Automovil
from apps.sucursales.models import Sucursales
#from apps.ventas_cotizaciones.models import Ventas


class VentasForm(forms.ModelForm):
    automovil = forms.ModelChoiceField(queryset=Automovil.objects.filter(cantidad__gte = 1))
    #valor_venta = forms.CharField( widget=forms.TextInput(attrs={'class':'disabled', 'readonly':'readonly'}))
    #vendedor = forms.ModelChoiceField(queryset=User.objects.filter(is_active=True, charge="Vendedor"))
    #sucursal = forms.ModelChoiceField(queryset=Sucursales.objects.filter(is_active=True))
    nombre_comprador=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'nameshoperInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    doc_id_comprador=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'IdInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    def save(self, *args, **kwargs):
        pk = self.cleaned_data['automovil'].id
        auto = Automovil.objects.get(pk=pk)
        self.cleaned_data['valor_venta'] = self.cleaned_data['automovil'].precio

        #print "VALOR DE LA VENTA ==> ", self.cleaned_data['valor_venta']
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

    nombre_comprador=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'nameshoperInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))
    doc_id_comprador=forms.CharField(max_length=50,widget = forms.TextInput(attrs={
                                                        'id':'IdInput',
                                                        'type':'text',
                                                        'class':'form-control'
                                   }))


    def asignar_vendedor_sucursal(self, vendedor_username):
        queryset_vendedor = User.objects.filter(username=vendedor_username)
        queryset_sucursal = Sucursales.objects.filter(pk=queryset_vendedor[0].branch_id)
        self.fields['vendedor'].queryset = queryset_vendedor
        self.fields['sucursal'].queryset = queryset_sucursal

    def save(self, *args, **kwargs):
        return super(CotizacionesForm, self).save(*args, **kwargs)

    def set_vendedor(self, vendedor_username):
        queryset = User.objects.filter(username=vendedor_username)
        self.fields['vendedor'].queryset = queryset
    
    class Meta:
        model = Cotizaciones
        fields = ('automovil', 'sucursal',  'vendedor', 'nombre_comprador', 'doc_id_comprador')

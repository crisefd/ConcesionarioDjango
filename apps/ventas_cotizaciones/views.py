from django.shortcuts import render, redirect
from django.utils import timezone
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .htmltopdf import generate_pdf
import datetime


context_pdf = {'vendedor':'waldo'}

class SaleRegisterView(SuccessMessageMixin, FormView):
    form_class = VentasForm
    template_name = 'registro_venta.html'
    success_url = '/venta/registro/'

    def get_form(self, form_class=None):
        f = super(SaleRegisterView, self).get_form(form_class)
        #print self.get_form_kwargs()
        f.asignar_vendedor_sucursal(self.request.user.username)
        return f

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 
            "No se ha podido registrar la venta " )
        return super(SaleRegisterView, self).form_valid(form)

    def form_valid(self, form):
        venta = form.save()

        self.success_url = '/factura_venta/'
        global context_pdf
        fecha_venta = datetime.datetime.now()
        context_pdf = {'vendedor': form.cleaned_data['vendedor'],
                        'sucursal': form.cleaned_data['sucursal'], 
                        'nombre_comprador': form.cleaned_data['nombre_comprador'],
                        'doc_id_comprador': form.cleaned_data['doc_id_comprador'],
                        'automovil': form.cleaned_data['automovil'],
                        'valor_venta': form.cleaned_data['valor_venta'],
                        'fecha': str(fecha_venta)
         }
        venta.valor_venta = form.cleaned_data['valor_venta']
        #venta = Ventas.objects.get(fecha=fecha_venta.strftime('%Y-%m-%d') vendedor )
        #venta.valor_venta = form.cleaned_data['valor_venta']
        venta.save()
        #print "Venta ", context_pdf
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la venta " )
        return super(SaleRegisterView, self).form_valid(form)


class QuoteRegisterView(SuccessMessageMixin, FormView):
    form_class = CotizacionesForm
    template_name = 'registro_cotizacion.html'
    success_url = '/cotizacion/registro/'

    def get_form(self, form_class=None):
        f = super(QuoteRegisterView, self).get_form(form_class)
        #print self.get_form_kwargs()
        f.asignar_vendedor_sucursal(self.request.user.username)
        return f

    def form_valid(self, form):
        print "formulario valido"
        form.save()
        self.success_url = '/recibo_consignacion/'
        global context_pdf
        context_pdf = {
                        'vendedor': form.cleaned_data['vendedor'],
                        'sucursal': form.cleaned_data['sucursal'], 
                        'nombre_comprador': form.cleaned_data['nombre_comprador'],
                        'doc_id_comprador': form.cleaned_data['doc_id_comprador'],
                        'automovil': form.cleaned_data['automovil'],
                        'fecha': str(timezone.now())
        }
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la cotizacion " )
        return super(QuoteRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        print "formulario invalido"
        messages.add_message(self.request, messages.SUCCESS, 
            "No se ha podido registrar la cotizacion " )
        return super(QuoteRegisterView, self).form_valid(form)

def pdf(request, template_name):
    return generate_pdf(template_name, context_pdf)
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

class SaleRegisterView(SuccessMessageMixin, FormView):
    form_class = VentasForm
    template_name = 'registro_venta.html'
    success_url = '/venta/registro/'

    def get_form(self, form_class=None):
        f = super(SaleRegisterView, self).get_form(form_class)
        #print self.get_form_kwargs()
        f.set_vendedor(self.request.user.username)
        return f

    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 
            "No se ha podido registrar la venta " )
        return super(SaleRegisterView, self).form_valid(form)

    def form_valid(self, form):
        form.save()
        pdf(self.request, form)
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
        f.set_vendedor(self.request.user.username)
        return f

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la cotizacion " )
        return super(QuoteRegisterView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 
            "No se ha podido registrar la cotizacion " )
        return super(QuoteRegisterView, self).form_valid(form)

def pdf(request, form):
    context = {'vendedor': form.cleaned_data['vendedor'], 
    'nombre_comprador': form.cleaned_data['nombre_comprador'],
    'automovil': form.cleaned_data['automovil'],
     'valor_venta': form.cleaned_data['valor_venta'],
     'fecha': str(timezone.now())
     }
    return generate_pdf("factura_venta.html", context)
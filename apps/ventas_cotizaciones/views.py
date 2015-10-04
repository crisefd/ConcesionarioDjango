from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

class SaleRegisterView(FormView):
    form_class = VentasForm
    template_name = 'registro_venta.html'
    success_url = '/venta/registro/'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la venta " )
        return super(SaleRegisterView, self).form_valid(form)


class QuoteRegisterView(FormView):
    form_class = CotizacionesForm
    template_name = 'registro_cotizacion.html'
    success_url = '/cotizacion/registro/'

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la cotizacion " )
        return super(QuoteRegisterView, self).form_valid(form)

from django.shortcuts import render, redirect, render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib import messages
from .forms import *


class RegistroSucursal(SuccessMessageMixin, FormView):
    form_class = SucursalesForm
    template_name = 'registro_sucursal.html'
    success_url = '/sucursal/registro/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registro de sucursal exitoso")
        return super(RegistroSucursal, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Registro de sucursal erroneo")
        return super(RegistroSucursal, self).form_valid(form)




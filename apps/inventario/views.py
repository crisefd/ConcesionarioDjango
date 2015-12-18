from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
from datatableview.views import DatatableView, XEditableDatatableView
from datatableview import helpers

class RegisterView(SuccessMessageMixin, FormView):

    def form_valid(self, form):
        print "Formulario valido"
        self.success_url = '/inventario/'
        if self.template_name == 'registro_automovil.html':
            self.success_url += 'automovil/registro/'
        else:
            self.success_url += 'repuesto/registro/'

        messages.success(self.request, 
            "Se ha registrado exitosamente el inventario " )
        form.save()
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        print "Formularion invalido", form.errors
        messages.error(self.request, 
            "Error, no se pudo registrar al inventario " + form.errors )
        return super(RegisterView, self).form_valid(form)

class AutoDataTableView(XEditableDatatableView):
    model = Automovil
    template_name = 'cars_list.html'
    datatable_options = {
        'columns': [
            ("Precio", 'precio', helpers.make_xeditable),
            ("Cantidad", 'cantidad', helpers.make_xeditable),
            ("Marca", 'marca', helpers.make_xeditable),
            ("Modelo", 'modelo', helpers.make_xeditable),
           ]
        }


class SpareDataTableView(XEditableDatatableView):
    model = Repuesto
    template_name = 'spares_list.html'
    datatable_options = {
        'columns': [
            ("Precio $(US Dollar)", 'precio', helpers.make_xeditable),
            ("Cantidad", 'cantidad', helpers.make_xeditable),
            ("Nombre", 'nombre', helpers.make_xeditable),
            ]
        }


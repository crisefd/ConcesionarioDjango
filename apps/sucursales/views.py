from django.shortcuts import render, redirect, render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
from datatableview.views import DatatableView, XEditableDatatableView
from datatableview import helpers


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


class BranchDatatableView(XEditableDatatableView):
    model = Sucursales
    template_name = 'branches_list.html'
    datatable_options = {
        'columns': [
            ("Nombre", 'nombre', helpers.make_xeditable),
            ("Direccion", 'direccion', helpers.make_xeditable),
            ("Activa", 'is_active', helpers.make_xeditable),
        ]
    }

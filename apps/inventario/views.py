from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


class RegisterView(SuccessMessageMixin, FormView):

    def form_valid(self, form):
        self.success_url = 'inventario/'
        if self.template_name == 'registro_automovil.html':
            self.success_url += 'automovil/registro/'
        else:
            self.success_url += 'repuesto/registro/'

        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Se ha registrado exitosamente el inventario " )

        return super(StockView, self).form_valid(form)


from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *


class RegisterView(SuccessMessageMixin, FormView):
    success_url = '/ordenes_trabajo/registro/'
    form_class = Ordenes_TrabajoForm
    template_name = 'registro_orden.html'
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 
            "Se ha registrado exitosamente la orden de trabajo " )

        return super(RegisterView, self).form_valid(form)


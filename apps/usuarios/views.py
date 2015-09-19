from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, MyUserCreationForm
"""
def hola_mundo(request):
    nombre_completo = "Cristhian Fuertes"
    return render(request, "hola_mundo.html", {"nombre_completo": nombre_completo}) 
"""

class IndexViewLogin(FormView):
    form_class = LoginForm
    template_name = 'index.html'
    succes_url = '/'
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(LoginView, self).form_valid(form)


class IndexViewRegister(FormView):
    form_class = MyUserCreationForm
    template_name = "registro_usuario.html"
    succes_url = "/registrar/"

    def form_valid(self, form):
        form.save()
        return super(IndexViewRegister, self).form_valid(form)

def LogOut(request):
    logout(request)
    return redirect('index.html')


def welcome(request):
    return redirect('welcome.html')
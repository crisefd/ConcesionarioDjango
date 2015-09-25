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

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    
    def form_valid(self, form):
        print "validando formulario"
        user = authenticate(username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password'])
        success_url = '/'
        if user is not None:
            print "el usuario ", user.username, "existe"
            if user.is_active:
                print "el usuario esta activo"
                if user.charge == "Gerente":
                    success_url += "cuentas/gerente/" + user.username
                login(self.request, user)
        return super(LoginView, self).form_valid(form)


class RegisterView(FormView):
    form_class = MyUserCreationForm
    template_name = "registro_usuario.html"
    succes_url = "/registro_completo/"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)


def inicio_gerente(request):
    return render(request, "inicio_gerente.html")

def registration_completed(request):
    return redirect('registro_completo.html')

def logOut(request):
    logout(request)
    return redirect('login.html')


def welcome(request):
    return redirect('welcome.html')
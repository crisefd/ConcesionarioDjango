from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, MyUserCreationForm
from django.contrib import messages

class LoginView(SuccessMessageMixin, FormView):
    form_class = LoginForm
    template_name = 'login.html'
    
    def form_valid(self, form):
        print "validando formulario"
        user = authenticate(username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password'])
        self.success_url = ''
        if user is not None:
            print "el usuario ", user.username, "existe"
            if user.is_active:
                print "el usuario esta activo"
                if user.charge == "Gerente":
                    self.success_url += "/cuentas/gerente/" + user.username
                elif user.charge == "Vendedor":
                    self.success_url += "/cuentas/vendedor/" + user.username
                else:
                    self.success_url += "cuentas/jefetaller/" + user.username
                messages.add_message(self.request, messages.SUCCESS, "Bienvenido " + user.username)
                login(self.request, user)
        return super(LoginView, self).form_valid(form)


class RegisterView(FormView):
    form_class = MyUserCreationForm
    template_name = "registro_usuario.html"
    succes_url = "/registrar/"

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Se ha registrado exitosamente al usuario " + user.username)
        return super(RegisterView, self).form_valid(form)



def inicio_gerente(request):
    return render(request, "inicio_gerente.html")


def inicio_vendedor(request):
    return render(request, "inicio_vendedor.html")

def inicio_jefetaller(request):
    return render(request, "inicio_jefetaller.html")


def logOut(request):
    logout(request)
    return render(request,'login.html')



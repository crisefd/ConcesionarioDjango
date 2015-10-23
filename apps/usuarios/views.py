from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, MyUserCreationForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth.views import password_change

class LoginView(SuccessMessageMixin, FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
    def form_valid(self, form):
        self.success_url = ''
        user = authenticate(username = form.cleaned_data['username'], 
                    password = form.cleaned_data['password'])
        if user is not None:
            #print "el usuario ", user.username, "existe"
            if user.is_active:
                #print "el usuario esta activo"
                if user.charge == "Gerente":
                    self.success_url += "/cuentas/gerente/" + user.username
                elif user.charge == "Vendedor":
                    self.success_url += "/cuentas/vendedor/" + user.username
                else:
                    self.success_url += "/cuentas/jefetaller/" + user.username
                messages.add_message(self.request, messages.SUCCESS, "Bienvenido " + user.username)
                login(self.request, user)
            else:
                self.success_url += '/login/'
                messages.add_message(self.request, messages.ERROR, "El usuario" + user.username + " no esta activo")
        else:
            self.success_url += '/login/'
            messages.add_message(self.request, messages.ERROR, "El usuario no existe")

        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Formulario incorrecto, revise nombre de usuario y contrasena")
        return super(LoginView, self).form_invalid(form)        


class RegisterView(SuccessMessageMixin, FormView):
    form_class = MyUserCreationForm
    template_name = "registro_usuario.html"
    success_url = "/registrar/"

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Se ha registrado exitosamente al usuario ")
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        print "formularion invalido"
        messages.add_message(self.request, messages.ERROR, "No se pudo registrar al usuario")
        return super(RegisterView, self).form_invalid(form)

class EditProfileView(SuccessMessageMixin, FormView):
    success_url = '/'
    form_class = EditProfileForm
    template_name = 'editar_perfil.html'

    def get_form(self, form_class=None):
        f = super(EditProfileView, self).get_form(form_class)
        #print self.get_form_kwargs()
        f.set_fields(self.request.user.username)
        return f

    def form_valid(self, form):
        charge = self.request.user.charge
        if charge == 'Jefe Taller':
            self.success_url = "/cuentas/jefetaller/" + self.request.user.username
            #self.template_name = "inicio_jefe_taller.html"
        elif charge == "Vendedor":
            self.success_url = "/cuentas/vendedor/" + self.request.username
            #self.template_name = "inicio_vendedor.html"
        messages.success(self.request, "Edicion exitosa")
        form.update()
        return super(EditProfileView, self).form_valid(form)

    def form_invalid(self, form):
        print "INVALIDO"
        messages.success(self.request, "Error al editar usuario")
        return super(EditProfileView, self).form_invalid(form)






def inicio_gerente(request):
    return render(request, "inicio_gerente.html")


def inicio_vendedor(request):
    return render(request, "inicio_vendedor.html")

def inicio_jefe_taller(request):
    return render(request, "inicio_jefe_taller.html")

def home(request):
    return render(request, "home.html")


def logOut(request):
    logout(request)
    #home(request)
    return redirect('/home')



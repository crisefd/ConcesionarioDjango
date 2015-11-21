from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, MyUserCreationForm, EditProfileForm
from django.contrib import messages
from django.http import JsonResponse

MIN_SEARCH_CHARS = 4

class LoginView(SuccessMessageMixin, FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.success_url = ''
        successful_log_in = False
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
                #messages.add_message(self.request, messages.SUCCESS, "Bienvenido " + user.username)
                login(self.request, user)
                #successful_log_in = True
                #if not self.request.POST.get('rem', None):
                #   self.request.session.set_expiry(0)
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
        elif charge == "Vendedor":
            self.success_url = "/cuentas/vendedor/" + self.request.user.username
        else:
            self.success_url = "/cuentas/gerente/" + self.request.user.username
        messages.success(self.request, "Edicion exitosa")
        form.update()
        return super(EditProfileView, self).form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Error al editar usuario")
        return super(EditProfileView, self).form_invalid(form)


class UserListView(SuccessMessageMixin, ListView):
    model = User
    context_object_name = "users"
    form_class = SearchUserForm

    def form_valid(self, form):
        search_text = form.cleaned_data['searchText']
        return search_users(self.request, search_text)

    def get_context_data(self, **kwargs):
        global MIN_SEARCH_CHARS
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context["MIN_SEARCH_CHARS"] = MIN_SEARCH_CHARS

        return  context

def search_users(request, user_id):
    """
    Processes a search request, ignoring any where less than four
    characters are provided. The search text is both trimmed and
    lower-cased.
    """
 
    search_results = []  #Assume no results.
 
    global  MIN_SEARCH_CHARS
 
    search_text = ""   #Assume no search
    if(request.method == "GET"):
        search_text = request.GET.get("search_text", "").strip().lower()
        if(len(search_text) < MIN_SEARCH_CHARS):
            """
            Ignore the search. This is also validated by
            JavaScript, and should never reach here, but remains
            as prevention.
            """
            search_text = ""
    if(search_text != ""):
        first_name_results = User.objects.filter(first_name__contains=search_text)
        last_name_results = User.objects.filter(last_name__contains=search_text)
        username_results = User.objects.filter(username_name__contains=search_text)
        email_results = User.objects.filter(email__contains=search_text)
        id_document_results = User.objects.filter(id_document__contains=search_text)
        search_results = first_name_results | last_name_results | username_results | email_results | id_document_results
 
    #print('search_text="' + search_text + '", results=' + str(color_results))
 
    context = {
        "search_text": search_text,
        "search_results": search_results,
        "MIN_SEARCH_CHARS": MIN_SEARCH_CHARS,
    };
 
    return  render_to_response("user_search_results.html",
                               context)


def inicio_gerente(request):
    return render(request, "inicio_gerente.html")


def inicio_vendedor(request):
    return render(request, "inicio_vendedor.html")

def inicio_jefe_taller(request):
    return render(request, "inicio_jefe_taller.html")

def password_change_done(request):
    url = ""
    if request.user.charge == 'Gerente':
        url = "/cuentas/gerente/" + request.user.username
    elif request.user.charge == 'Jefe Taller':
        url = "/cuentas/jefetaller/" + request.user.username
    else:
        url = "/cuentas/vendedor/" + request.user.username
    return redirect(url)





def logOut(request):
    logout(request)
    #home(request)
    return redirect('/home')



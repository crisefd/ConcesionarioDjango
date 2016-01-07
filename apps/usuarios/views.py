from django.shortcuts import render, redirect, render_to_response
from django.template import Template, Context
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import FormView, ListView
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from .models import User
from apps.sucursales.models import Sucursales
from django.http import JsonResponse
from datatableview.views import DatatableView, XEditableDatatableView
from datatableview import helpers
import json as simplejson
import datetime
from apps.ventas_cotizaciones.models import Ventas
from apps.inventario.models import Automovil
from django.db.models import Count
from django.db.models import Sum



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
                    self.success_url += "/cuentas/Gerente/" + user.username
                elif user.charge == "Vendedor":
                    self.success_url += "/cuentas/Vendedor/" + user.username
                else:
                    self.success_url += "/cuentas/Jefetaller/" + user.username
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
            self.success_url = "/cuentas/Jefetaller/" + self.request.user.username
        elif charge == "Vendedor":
            self.success_url = "/cuentas/Vendedor/" + self.request.user.username
        else:
            self.success_url = "/cuentas/Gerente/" + self.request.user.username
        messages.success(self.request, "Edicion exitosa")
        form.update()
        return super(EditProfileView, self).form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Error al editar usuario")
        return super(EditProfileView, self).form_invalid(form)





class UserDatatableView(XEditableDatatableView):
    model = User
    template_name = 'user_list.html'
    datatable_options = {
        'columns': [
            ("Nombres", 'first_name', helpers.make_xeditable),
            ("Apellidos", 'last_name', helpers.make_xeditable),
            ("Nombre de usuario", 'username', helpers.make_xeditable),
            ("e-mail", 'email', helpers.make_xeditable),
            ("Doc ID", 'id_document', helpers.make_xeditable),
            ("Nacimiento", 'birth_date', helpers.make_xeditable),
            ("Direccion", 'address', helpers.make_xeditable),
            ("Telefono", 'phone_number', helpers.make_xeditable),
            ("Cargo", 'charge', helpers.make_xeditable),
            ("Activo", 'is_active', helpers.make_xeditable),

        ]
    }




def mes(m):
    ls1 = [ "Enero" ,
              "Febrero",
              "Marzo",
              "Abril",
              "Mayo",
              "Junio",
              "Julio",
              "Agosto",
              "Septiembre",
              "Octubre",
              "Noviembre",
              "Diciembre",
    ]

    ls2 = {  "Enero":0 ,
              "Febrero":1,
              "Marzo":2,
              "Abril":3,
              "Mayo":4,
              "Junio":5,
              "Julio":6,
              "Agosto":7,
              "Septiembre":8,
              "Octubre":9,
              "Noviembre":10,
              "Diciembre":11,
    }
    if type(m) == type(4):
        return ls1[m]
    elif type(m) == type("a"):
        return ls2[m]

def consultar_ventas_sucursales(ano_actual, mes_actual, fechas_permitidas, sucursales):
    fecha_ignorar = datetime.date(ano_actual-2,  12, 31)
    items = list(Ventas.objects.exclude(fecha__lte=fecha_ignorar).values('sucursal', 'fecha').annotate(num_ventas=Count('sucursal')).order_by('fecha'))
    #print "==> fechas permitidas ", fechas_permitidas
    banderas_f_permitidas = [0]*len(fechas_permitidas)
    salida = {}
    for item in items:
        i = 0
        for f in fechas_permitidas:
            if item['fecha'].year == f.year and item['fecha'].month == f.month:
                fecha = str(f.year)+"-"+str(f.month)+"-1"
                banderas_f_permitidas[i] = 1
                clave = Sucursales.objects.get(pk=item['sucursal']).nombre.encode()
                if clave in salida:
                    salida[clave].append({'fecha':fecha,
                        'num_ventas': item['num_ventas']})
                else:
                    salida[clave] = [{'fecha':fecha,
                        'num_ventas': item['num_ventas']}]
            i += 1
   

    return ordenar_salida_ventas(salida)

def ordenar_salida_ventas(salida):
    salida_ordenada = {}
    for clave, valor in salida.iteritems():
        #print "VALOR ", valor
        salida_ordenada[clave] = sorted(valor, key= lambda item: item['fecha'])
    return salida_ordenada



"""Reporte Ventas"""
def fechas_permitidas(ano_actual, num_mes_actual):
    def foo(m):
        ls = [1,2,3,4,5,6,7,8,9,10,11,12]
        return ls[m]

    m = num_mes_actual
    ano = ano_actual
    fechas = []
    for i in range(0, 12):
        if m == 0:
            ano -= 1
        mes = foo(m - 1)
        fechas.append(datetime.date(ano, mes, 1))
        m -= 1
    return fechas

def obtener_meses(num_mes_actual):
    respueta_meses = []
    for i in range(0, 12):
        respueta_meses.append(mes(num_mes_actual - i))
    return respueta_meses

def reporte_ventas(contexto):
    num_mes_actual = datetime.datetime.now().month
    ano_actual = datetime.datetime.now().year
    meses = obtener_meses(num_mes_actual - 1)
    meses = meses[::-1]
    #print "meses ==>", len(meses), meses
    sucursales = list(Sucursales.objects.filter(is_active=True))
    #print "sucursales ==>", len(sucursales),sucursales
    fechas_permit = fechas_permitidas(ano_actual, num_mes_actual)
    ventas_sucursales = consultar_ventas_sucursales(ano_actual, 
        num_mes_actual, fechas_permit, sucursales)
    #print "ventas_sucursales ==>", len(ventas_sucursales),ventas_sucursales
    nombre_sucursales = list(Sucursales.objects.values('nombre').filter(is_active=True))
    for i in range(0, len(nombre_sucursales)):
        nombre_sucursales[i] = nombre_sucursales[i]['nombre'].encode()
    #print "sucursales ==>", len(nombre_sucursales), nombre_sucursales
    contexto['meses'] = simplejson.dumps(meses)
    contexto['sucursales'] = simplejson.dumps(nombre_sucursales)
    contexto['ventas_sucursales'] = simplejson.dumps(ventas_sucursales)

"""Reporte Inventario"""

def consultar_automoviles():
    consulta_autos = list(Automovil.objects.values('marca', 'cantidad').filter(cantidad__gte=1))
    total_autos = Automovil.objects.all().aggregate(Sum('cantidad'))
    consulta_autos.append(total_autos)
    for i in range(0, len(consulta_autos) - 1):
        consulta_autos[i]['marca'] = consulta_autos[i]['marca'].encode()
    return consulta_autos

def calcular_porcentaje_autos(consulta_autos):
    total_autos = consulta_autos[-1]['cantidad__sum']
    for i in range(0, len(consulta_autos)-1):
        consulta_autos[i]['porcentaje'] = 1.0*consulta_autos[i]['cantidad']/(total_autos) 

def reporte_inventario(contexto):
    consulta_autos = consultar_automoviles()
    calcular_porcentaje_autos(consulta_autos)
    print "consulta autos ==> ", consulta_autos
    contexto['consulta_autos'] = simplejson.dumps(consulta_autos)


def inicio_gerente(request):
    contexto = {}
    reporte_ventas(contexto)
    reporte_inventario(contexto)
    return render(request, "inicio_gerente.html", contexto)


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



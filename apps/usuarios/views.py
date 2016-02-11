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
from apps.inventario.models import Automovil, Repuesto
from apps.ordenes_trabajo.models import *
from django.db.models import Count, Sum
from django.db import connection
truncate_date = connection.ops.date_trunc_sql('month', 'fecha')



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
    consulta_autos = list(Automovil.objects.values('marca').filter(cantidad__gte=1).annotate(cantidad_total=Sum('cantidad')).order_by('marca'))
    total_autos = Automovil.objects.all().aggregate(Sum('cantidad'))
    consulta_autos.append(total_autos)
    print "consulta_autos ", consulta_autos
    for i in range(0, len(consulta_autos) - 1):
        consulta_autos[i]['marca'] = consulta_autos[i]['marca'].encode()
    return consulta_autos

def calcular_porcentaje_autos(consulta_autos):
    total_autos = consulta_autos[-1]['cantidad__sum']
    for i in range(0, len(consulta_autos)-1):
        consulta_autos[i]['porcentaje'] = 1.0*consulta_autos[i]['cantidad_total']/(total_autos)

def consultar_repuestos():
    consulta_repuestos = list(Repuesto.objects.values('marca').filter(cantidad__gte=1).annotate(cantidad_total=Sum('cantidad')).order_by('marca'))
    total_repuestos = Repuesto.objects.all().aggregate(Sum('cantidad'))
    consulta_repuestos.append(total_repuestos)
    for i in range(0, len(consulta_repuestos) - 1):
        consulta_repuestos[i]['marca'] = consulta_repuestos[i]['marca'].encode()
    return consulta_repuestos

def calcular_porcentaje_repuestos(consulta_repuestos):
    total_repuestos = consulta_repuestos[-1]['cantidad__sum']
    for i in range(0, len(consulta_repuestos)-1):
        consulta_repuestos[i]['porcentaje'] = 1.0*consulta_repuestos[i]['cantidad_total']/(total_repuestos) 

def reporte_inventario(contexto):
    consulta_autos = consultar_automoviles()
    calcular_porcentaje_autos(consulta_autos)
    consulta_repuestos = consultar_repuestos()
    calcular_porcentaje_repuestos(consulta_repuestos)
    #print "consulta repuestos ==> ", consulta_repuestos
    contexto['consulta_autos'] = simplejson.dumps(consulta_autos)
    contexto['consulta_repuestos'] = simplejson.dumps(consulta_repuestos)

"""Reporte Vendedores"""

def encontrar_mejor_vendedor_sucursal(consulta_vendedores, sucursal):
    nombre_sucursal = sucursal.nombre
    mejor_vendedor = None
    #k = 0
    for item in consulta_vendedores:
        if item['sucursal'] == nombre_sucursal:
            if mejor_vendedor is None:
                mejor_vendedor = item
            elif item['num_ventas'] > mejor_vendedor['num_ventas']:
                mejor_vendedor = item
        #k += 1
    if mejor_vendedor is None:
        mejor_vendedor = {}
    return mejor_vendedor




def consultar_ventas_vendedores():
    fecha_ignorar = None
    fecha_actual = datetime.datetime.now()
    if fecha_actual.month == 1:
        fecha_ignorar = datetime.date(fecha_actual.year - 1, 12, 31)
    elif fecha_actual.month == 3:
        fecha_ignorar = datetime.date(fecha_actual.year, 2, 28) # No valida anos bisiestos
    elif fecha_actual.month == 2 or fecha_actual.month == 4 or fecha_actual.month == 6 or fecha_actual.month == 8 or fecha_actual.month == 9 or fecha_actual.month == 11:
        fecha_ignorar = datetime.date(fecha_actual.year, fecha_actual.month - 1, 31)
    else:
        fecha_ignorar = datetime.date(fecha_actual.year, fecha_actual.month - 1, 30)
    print "fecha ignorar ==> ", fecha_ignorar

    consulta_vendedores = list(Ventas.objects.exclude(fecha__lte=fecha_ignorar).values('sucursal',
        'vendedor').annotate(num_ventas=Count('vendedor')).order_by('num_ventas'))
    #print "consulta_vendedores ", consulta_vendedores
    for i in range(0, len(consulta_vendedores)):
        id_vendedor = consulta_vendedores[i]['vendedor']
        id_sucursal = consulta_vendedores[i]['sucursal']
        vendedor = User.objects.get(pk=id_vendedor)
        sucursal = Sucursales.objects.get(pk=id_sucursal)
        consulta_vendedores[i]['vendedor'] = vendedor.first_name.encode() + " " + vendedor.last_name.encode()
        consulta_vendedores[i]['sucursal'] = sucursal.nombre.encode()

    #print "consulta_vendedores ", consulta_vendedores
    sucursales = Sucursales.objects.filter(is_active=True) # No se validan sucursales inactivas
    salida = {}
    for sucursal in sucursales:
        clave = sucursal.nombre.encode()
        #print "clave ==>", str(clave)
        salida[str(clave)] = encontrar_mejor_vendedor_sucursal(consulta_vendedores, sucursal)

    #print "salida ", salida
    return salida

def reporte_vendedores(contexto):
    consulta_vendedores = consultar_ventas_vendedores()
    contexto['consulta_vendedores'] = simplejson.dumps(consulta_vendedores)
    #print "consulta vendedores ==> ", consulta_vendedores


""" Reporte Ganancias """

def consultar_ganancias(ano_actual, fechas_permitidas):
    now = datetime.datetime.now()
    fecha_ignorar_superior = datetime.date(now.year,  now.month, now.day)
    def aux(mes, ano):
        if mes == 12:
            return datetime.date(ano, 1, 1)
        else:
            return datetime.date(ano - 1, mes + 1, 1)
    #print datetime.datetime.now().month
    fecha_ignorar_inferior = aux( now.month, ano_actual)
    #print "fecha ignorar inferior ", fecha_ignorar_inferior
    qs = Ventas.objects.extra({'month':truncate_date})
    #print "QS ==> ", qs
    consulta_ganancias = list(qs.values('month').exclude(fecha__lt=fecha_ignorar_inferior).annotate(ganancia=Sum('valor_venta')).order_by('month'))
    #print "XXXXXX ", consulta_ganancias
    for i in range(0, len(consulta_ganancias)):
        consulta_ganancias[i] = {'ganancia':consulta_ganancias[i]['ganancia']}

    
    return consulta_ganancias


def reporte_ganancias(contexto):
    num_mes_actual = datetime.datetime.now().month
    ano_actual = datetime.datetime.now().year
    meses = obtener_meses(num_mes_actual - 1)
    meses = meses[::-1]
    fechas_permit = fechas_permitidas(ano_actual, num_mes_actual)
    consulta_ganancias = consultar_ganancias(ano_actual, fechas_permit)
    #print "consulta_ganancias ==> ",len(consulta_ganancias), consulta_ganancias
    #print "meses ==> ", meses
    contexto['meses_ganancias'] = simplejson.dumps(meses)
    contexto['consulta_ganancias'] = simplejson.dumps(consulta_ganancias)


""" Reporte ordenes"""


def consultar_ordenes():
    fecha_actual = datetime.datetime.now()
    fecha_ignorar = None
    if fecha_actual.month == 1:
        fecha_ignorar = datetime.date(fecha_actual.year - 1, 12, 31)
    elif fecha_actual.month == 3:
        fecha_ignorar = datetime.date(fecha_actual.year, 2, 28)
    elif fecha_actual.month == 2 or fecha_actual.month == 4 or fecha_actual.month == 6 or fecha_actual.month == 8 or fecha_actual.month == 9 or fecha_actual.month == 11:
        fecha_ignorar = datetime.date(fecha_actual.year, fecha_actual.month - 1, 31)
    else:
        fecha_ignorar = datetime.date(fecha_actual.year, fecha_actual.month - 1, 30)

    consulta_ordenes = list(Orden_Repuesto.objects.values('orden_id__jefe_taller_id__branch_id__nombre').exclude(fecha__lte=fecha_ignorar).annotate(cantidad=Count('id')))

    salida = []
    print "len ", len(consulta_ordenes)
    for i in range(0, len(consulta_ordenes)):
        #print "i=", i
        salida.append({'sucursal':str(consulta_ordenes[i]['orden_id__jefe_taller_id__branch_id__nombre']), 'cantidad':consulta_ordenes[i]['cantidad']})
        #print "i=", i
    return salida

def reporte_ordenes(contexto):
    contexto['consulta_ordenes'] = simplejson.dumps(consultar_ordenes())

 

def inicio_gerente(request):
    contexto = {}
    reporte_ventas(contexto)
    reporte_inventario(contexto)
    reporte_vendedores(contexto)
    reporte_ganancias(contexto)
    reporte_ordenes(contexto)
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



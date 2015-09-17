from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
# Create your views here.

def hola_mundo(request):
	nombre_completo = "Cristhian Fuertes"
	return render(request,
					"hola_mundo.html",
					{"nombre_completo": nombre_completo}
					) 

def login(request):
	pass

def registro(request):
	pass
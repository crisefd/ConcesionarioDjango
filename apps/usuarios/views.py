from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
# Create your views here.

def hola_mundo(request):
	contenido =  "<html><body>Hola Mundo!.</body></html>"
	t = Template(contenido)
	html = t.render(Context({}))
	return HttpResponse(html)

def login(request):
	pass

def registro(request):
	pass
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse

def show_home(request):
    return render(request, 'home.html')

from django.contrib import admin
from .models import *

@admin.register(Ventas, Cotizaciones)
class ModelosAdmin(admin.ModelAdmin):
    pass
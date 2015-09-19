from django.contrib import admin
from .models import *

@admin.register(Ordenes_Trabajo, Cotizaciones, Ventas, Repuesto, Automovil, Mecanicos, Sucursales)
class ModelosAdmin(admin.ModelAdmin):
    pass
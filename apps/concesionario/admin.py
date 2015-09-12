from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sucursales)
admin.site.register(Mecanicos)
admin.site.register(Automovil)
admin.site.register(Ventas)
admin.site.register(Cotizaciones)
admin.site.register(Ordenes_Trabajo)
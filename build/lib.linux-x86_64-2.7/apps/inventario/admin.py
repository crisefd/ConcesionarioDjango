from django.contrib import admin
from .models import *

@admin.register(Automovil, Repuesto)
class ModelosAdmin(admin.ModelAdmin):
    pass
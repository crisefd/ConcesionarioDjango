from django.contrib import admin
from .models import *

@admin.register(Mecanicos, Ordenes_Trabajo)
class ModelosAdmin(admin.ModelAdmin):
    pass
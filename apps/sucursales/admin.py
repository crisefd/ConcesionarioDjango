from django.contrib import admin
from .models import *

@admin.register(Sucursales)
class ModelosAdmin(admin.ModelAdmin):
    pass
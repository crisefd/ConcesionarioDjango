from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(User, Vendedor_Sucursal, JefeTaller_Sucursal)
class Admin(admin.ModelAdmin):
    pass
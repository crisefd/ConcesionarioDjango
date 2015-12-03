from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
   url(r'^sucursal/registro/$', RegistroSucursal.as_view(), name="registro_sucursal"),
)
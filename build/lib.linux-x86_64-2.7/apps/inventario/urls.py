from django.conf.urls import patterns, url
from .views import *
from .forms import *


urlpatterns = patterns('',
    url(r'^inventario/automovil/registro/$', RegisterView.as_view(template_name='registro_automovil.html',
                                            form_class=AutomovilForm), name='registro_automovil'),
    url(r'^inventario/repuesto/registro/$',  RegisterView.as_view(template_name='registro_repuesto.html',
                                            form_class=RepuestoForm), name='registro_automovil'),
    url(r'^inventario/autmovil/buscar/$', AutoDataTableView.as_view()),
    url(r'^inventario/repuesto/buscar/$', SpareDataTableView.as_view()),
)
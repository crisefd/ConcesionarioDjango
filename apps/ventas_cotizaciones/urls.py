from django.conf.urls import patterns, url
from .views import *
from .forms import *

urlpatterns = patterns('',
    url(r'^cotizacion/registro/$', QuoteRegisterView.as_view()),
    url(r'^venta/registro/$', SaleRegisterView.as_view()),
    url(r'^factura_venta/$', pdf,{'template_name':'factura_venta.html'}),
    url(r'^recibo_consignacion/$', pdf,{'template_name':'recibo_consignacion.html'}),
)

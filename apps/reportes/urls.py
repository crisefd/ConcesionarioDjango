from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^prueba_reporte/$', report_view, name='prueba_reporte'),
)
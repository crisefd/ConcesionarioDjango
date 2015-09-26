from django.conf.urls import include, url
from django.contrib import admin


urlpatterns=[
			url(r'^admin/',include(admin.site.urls)),
			url(r'^', include('apps.usuarios.urls',namespace='usuarios')),
            url(r'^', include('apps.inventario.urls',namespace='inventario')),
            #url(r'^', include('apps.sucursales.urls',namespace='usuarios')),
            #url(r'^', include('apps.ventas_cotizaciones.urls',namespace='usuarios')),
            #url(r'^', include('apps.ordenes_trabajo.urls',namespace='usuarios')),
			]


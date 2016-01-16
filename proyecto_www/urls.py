from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings


urlpatterns=[
			url(r'^admin/',include(admin.site.urls)),
            url(r'^accounts/', include('django.contrib.auth.urls')),
            url(r'^', include('apps.home.urls',namespace='home')),
			url(r'^', include('apps.usuarios.urls',namespace='usuarios')),
            url(r'^', include('apps.inventario.urls',namespace='inventario')),
            url(r'^', include('apps.ventas_cotizaciones.urls',namespace='ventas_cotizaciones')),
            url(r'^', include('apps.ordenes_trabajo.urls',namespace='ordenes_trabajo')),
            url(r'^', include('apps.sucursales.urls', namespace='sucursales')),
            url(r'^', include('apps.reportes.urls', namespace='reportes')),
			]

urlpatterns += url('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
#urlpatterns += staticfiles_urlpatterns()
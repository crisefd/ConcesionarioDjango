from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
	#url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^cuentas/gerente/[^/]+$', 'apps.usuarios.views.inicio_gerente', name='inicio_gerente'),
    url(r'^cuentas/gerente/[^/]+$', 'apps.usuarios.views.inicio_vendedor', name='inicio_vendedor'),
    url(r'^cuentas/gerente/[^/]+$', 'apps.usuarios.views.inicio_gerente', name='inicio_jefetaller'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^registrar/$', RegisterView.as_view()),
    #url(r'^registro_completo/$', 'apps.usuarios.views.registration_completed'),
    url(r'^salir/$','apps.usuarios.views.logOut'),
)
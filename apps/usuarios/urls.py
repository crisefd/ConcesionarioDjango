from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
	#url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^cuentas/gerente/[^/]+$', 'apps.usuarios.views.inicio_gerente', name='inicio_gerente'),
    url(r'^cuentas/vendedor/[^/]+$', 'apps.usuarios.views.inicio_vendedor', name='inicio_vendedor'),
    url(r'^cuentas/jefetaller/[^/]+$', 'apps.usuarios.views.inicio_jefe_taller', name='inicio_jefe_taller'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^home/$', 'apps.usuarios.views.home', name='home'),
    url(r'^registrar/$', RegisterView.as_view()),
    url(r'^salir/$','apps.usuarios.views.logOut'),
)
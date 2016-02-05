from django.conf.urls import patterns, include, url
#from django.contrib.auth.forms import PasswordChangeForm
from .views import *


urlpatterns = patterns('',
    url(r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'password_change_form': MyPasswordChangeForm, 'template_name':'password_change_form.html', 'post_change_redirect':'password_change_done'},
        name="password_change"),
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^password_change_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'password_change_done.html'},
        name='password_change_done'),
    url(r'^cuentas/Gerente/[^/]+$', 'apps.usuarios.views.inicio_gerente', name='inicio_gerente'),
    url(r'^cuentas/Vendedor/[^/]+$', 'apps.usuarios.views.inicio_vendedor', name='inicio_vendedor'),
    url(r'^cuentas/Jefetaller/[^/]+$', 'apps.usuarios.views.inicio_jefe_taller', name='inicio_jefe_taller'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^registrar/$', RegisterView.as_view()),
    url(r'^usuarios/busqueda/$', UserDatatableView.as_view(), name="user_list"),
    url(r'^cuentas/editar_perfil/[^/]+$', EditProfileView.as_view(), name="editar_perfil"),
    url(r'^salir/$','apps.usuarios.views.logOut'),
    
)
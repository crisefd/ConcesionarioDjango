from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from .views import *


urlpatterns = patterns('',
    url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change',
        {'password_change_form': AdminPasswordChangeForm, 'template_name':'password_change_form.html'},
        name="password_change"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/password_change_done/$', password_change_done,
        {'template_name': 'userauth/password_change_done.html'},
        name='userauth_password_change_done'),
    url(r'^cuentas/gerente/[^/]+$', 'apps.usuarios.views.inicio_gerente', name='inicio_gerente'),
    url(r'^cuentas/vendedor/[^/]+$', 'apps.usuarios.views.inicio_vendedor', name='inicio_vendedor'),
    url(r'^cuentas/jefetaller/[^/]+$', 'apps.usuarios.views.inicio_jefe_taller', name='inicio_jefe_taller'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^registrar/$', RegisterView.as_view()),
    url(r'^usuarios/busqueda/resultados/$', search_users, name="user_list"),
    url(r'^usuarios/busqueda/$', UserListView.as_view(), name="user_list"),
    url(r'^cuentas/editar_perfil/[^/]+$', EditProfileView.as_view(), name="editar_perfil"),
    url(r'^salir/$','apps.usuarios.views.logOut'),
)

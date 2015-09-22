from django.conf.urls import patterns, url
from .views import *


urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^accounts/profile/$', LoginView.as_view()),
    url(r'^registrar/$', RegisterView.as_view()),
    url(r'^registro_completo/$', 'apps.usuarios.views.registration_completed'),
    url(r'^salir/$','apps.usuarios.views.logOut'),
]
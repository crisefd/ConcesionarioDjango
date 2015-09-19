from django.conf.urls import patterns, url
from .views import IndexView


urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^accounts/profile/$', IndexView.as_view()),
    url(r'^salir$','apps.usuarios.views.LogOut'),
]
from django.conf.urls import patterns, url

urlpatterns = [
	url(r'^$', 'apps.usuarios.views.login'),
]
from django.conf.urls import patterns, url
from .views import *


urlpatterns = patterns('',
    url(r'^home/$', show_home, name='show_home'),
)
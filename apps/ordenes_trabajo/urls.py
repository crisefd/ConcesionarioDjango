from django.conf.urls import patterns, url
from .views import *
from .forms import *

urlpatterns = patterns('',
    url(r'^ordenes_trabajo/registro/$', RegisterView.as_view(), name='registro_orden'),
)

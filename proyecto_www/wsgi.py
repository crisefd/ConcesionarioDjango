"""
WSGI config for proyecto_www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling


#try:
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_www.settings.staging")
    #application = Cling(get_wsgi_application())
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(get_wsgi_application())
 #   print "whitenoise"
#except:
 #   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto_www.settings.local")
 #   application = get_wsgi_application()
  #  print "wsgi"
#application = DjangoWhiteNoise(application)

from .base import *


import dj_database_url
DATABASES['default'] =  dj_database_url.config()
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

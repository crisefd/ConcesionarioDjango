from .base import *

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG = True
TEMPLATE_DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
     'default':{
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME' : 'd5uvpg5dj9g35b',
    'USER' : 'ckodvufbczcflz',
    'PASSWORD' : '6myNkz2Fx7ifEWFriz073wqGhY',
    'HOST' : 'ec2-54-83-61-45.compute-1.amazonaws.com',
    'PORT' : '5432',
    }

}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

#STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
#STATICFILES_DIRS=(BASE_DIR,'static')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR.child('media')


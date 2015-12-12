from .base import *

DEBUG_TOOLBAR_PATCH_SETTINGS = False 

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
     'default':{
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'NAME' : 'd5odh3danbfh7g',
	'USER' : 'ojgwvdsjgzsyze',
	'PASSWORD' : 'vRpSaHV9c06O5fxcekFjyYxVek',
	'HOST' : 'ec2-54-83-59-110.compute-1.amazonaws.com',
	'PORT' : '5432'
	}
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=(BASE_DIR,'static',)


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


from .base import *

DEBUG_TOOLBAR_PATCH_SETTINGS = False 

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
   
    'default':{
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'NAME' : 'd7jighg3mjc5q7',
	'USER' : 'sppajfgaanmrif',
	'PASSWORD' : '93wRXO2OFE92nRGFoghli3AFrY',
	'HOST' : 'ec2-54-83-59-203.compute-1.amazonaws.com',
	'PORT' : '5432'
	}
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = STATIC_ROOT = 'static'


STATIC_URL = '/static/'

STATICFILES_DIRS=(BASE_DIR,'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


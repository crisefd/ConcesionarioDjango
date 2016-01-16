from .base import *

DEBUG_TOOLBAR_PATCH_SETTINGS = False 

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
   
    'default':{
	'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'NAME' : 'd5o4666qu9bqp6',
	'USER' : 'cjjnzgcfupjjty',
	'PASSWORD' : 'nzM-W9TFc9NtsFTZ_ufITeB0yR',
	'HOST' : 'ec2-54-225-165-132.compute-1.amazonaws.com',
	'PORT' : '5432'
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


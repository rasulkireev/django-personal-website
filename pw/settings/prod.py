from pw.settings.base import *

### Do not forget to set the environment settings variable to this file (on the server)
###### export DJANGO_SETTINGS_MODULE = pw.settings.prod

import os
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

# S3 Static settings
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static/'), ]
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'settings.storage_backends.StaticStorage'
# STATIC_URL = "https://%s/static/" % (AWS_S3_CUSTOM_DOMAIN)


MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'settings.storage_backends.MediaStorage'

# MEDIA_URL = 'https://%s/media/' % (AWS_S3_CUSTOM_DOMAIN)
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
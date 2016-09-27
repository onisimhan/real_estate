"""
Django settings for realestate project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config
from dj_database_url import parse as dburl
import urlparse
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = 'q3%c!jf8i5z45dt)6urxh35ect+oqc9##mmax%#5cpl7nlph_5'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['seethisproperty.com', 'www.seethisproperty.com', '148.251.15.39', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'realestate',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrapform',
    'compressor',
    'storages',
    'django.contrib.humanize',
    'opbeat.contrib.django',
)

MIDDLEWARE_CLASSES = (
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


ROOT_URLCONF = 'realestate.urls'

WSGI_APPLICATION = 'realestate.wsgi.application'

OPBEAT = {
    'ORGANIZATION_ID': '67b696028d2e4c6f9230db817a79d7e1',
    'APP_ID': '8bb83c3bde',
    'SECRET_TOKEN': 'e84b7467bacfe51ae64a22e9cb060a799873b0eb',
}

# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': config('DATABASE_URL', default=default_dburl, cast=dburl),
}

default_cache = 'redis://x:@127.0.0.1:6379'
redis_url = urlparse.urlparse(config('REDIS_URL', default=default_cache))

if DEBUG:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': "{0}:{1}".format(redis_url.hostname, redis_url.port),
            'OPTIONS': {
                'DB': 0,
                'PASSWORD': redis_url.password,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'CONNECTION_POOL_CLASS_KWARGS': {
                    'max_connections': 25,
                    'timeout': 4,
                }
            },
        },
    }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = config('STATIC_URL', default='/static/')
# 'http://seethisproperty-static-dir.e7bdqjqzfgrkl9rf7exoosh97egthfg5d5mpvbjb.netdna-cdn.com/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

EMAIL_USE_SSL = False
EMAIL_USE_TLS = False
EMAIL_HOST = 'mail.seethisproperty.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contact@seethisproperty.com'
EMAIL_HOST_PASSWORD = '2vdn8bhm1k'
DEFAULT_FROM_EMAIL = 'contact@seethisproperty.com'

COMPRESS_ENABLED = True
COMPRESS_AUTO = True
COMPRESS_VERSION = True

COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = True

# Set storage to AWS S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = 'seethisproperty-images'
AWS_ACCESS_KEY_ID = 'AKIAIM3GJJLHCVLC53TA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_HOST = 's3-accelerate.amazonaws.com'

TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.request",)


if DEBUG:
    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

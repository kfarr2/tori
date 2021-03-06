"""
Django settings for tori project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, hashlib
from varlet import variable

try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError as e:
    pass

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as messages
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, LOGGING, AUTHENTICATION_BACKENDS

here = lambda *path: os.path.normpath(os.path.join(os.path.dirname(__file__), *path))
ROOT = lambda *path: here("../", *path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = variable('SECRET_KEY', default=hashlib.sha1(os.urandom(64)).hexdigest())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = variable('DEBUG', default=True)

TEMPLATE_DEBUG = variable('TEMPLATE_DEBUG', default=True)

TEMPLATE_DIRS = (
    here("templates"),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tori.home',
    'tori.ipa',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tori.urls'

WSGI_APPLICATION = 'tori.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': variable("ENGINE", default='django.db.backends.mysql'),
        'NAME': variable("NAME", default=''),
        'USER': variable("USER", default='root'),
        'PASSWORD': variable("PASSWORD", default=''),
        'HOST': variable("HOST", default='localhost'),
        'PORT': variable("PORT", default=''),
    }
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

STATIC_URL = '/static/'

STATIC_ROOT = ROOT('static')

STATICFILES_DIRS = (
    here('static'),
)

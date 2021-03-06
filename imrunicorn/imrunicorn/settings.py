"""
Django settings for imrunicorn project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import socket
import os
from decouple import config, AutoConfig


import logging
import logging.config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = AutoConfig(search_path=BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hmj=u6w0i830gw=k^l&vc*jsl!mvtx8#r%#con#lvz04aordkg'
# IPRESTRICT_GEOIP_ENABLED = False

if socket.gethostname().find('MacBook') != -1 \
    or socket.gethostname().find('wk-benspelledabc') != -1:
    DEBUG = True
else:
    DEBUG = False
IS_PRODUCTION = not DEBUG

ALLOWED_HOSTS = ['benspelledabc.me', 'localhost', '127.0.0.1', '*']

# RESTRICT_IPS = True
# in settings.py (will override the above environment variable)
# ALLOWED_IPS = ['192.168.2.0/24', '192.168.0.1', '192.168.0.2', '192.168.0.3']
# ALLOW_AUTHENTICATED = True
# ALLOW_ADMIN = True
# RESTRICT_ADMIN_BY_IPS = True
# ALLOWED_ADMIN_IPS = ['192.168.2.0/24', '192.168.0.1', '192.168.0.2', '192.168.0.3']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'django_createsuperuserwithpassword',
    'django_extensions',
    'crispy_forms',
    'phone_field',
    'imrunicorn',
    'api',
    'loaddata',
    'farminvite',
    'announcements',
    'polls',
    'shooting_logbook',
    'groundhog_logbook',
    'admin_toolbox',
    'deer_harvest_logbook',
    'deer_wait_list',
    'status_watcher',
    'content_collection',
    'call_of_the_wild',
    'activity_log',
    'shooting_challenge',
    # 'rest_framework_swagger',
    # 'iprestrict',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ip_restriction.IpWhitelister',
]

ROOT_URLCONF = 'imrunicorn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'imrunicorn.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if socket.gethostname().startswith('benspelledabc') \
        or socket.gethostname().startswith('dell') \
        or socket.gethostname().startswith('docker-'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'OPTIONS': {
                'read_default_file': '/opt/loaddata.cnf',
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
elif socket.gethostname().startswith('unicorn_'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'imrunicorn',
            'USER': "imrunicorn",
            'PASSWORD': "imrunicorn",
            'HOST': "unicorn_db",
            'PORT': 3306,
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
        },
    }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# Default permission for all the rest framework things
# restrict to authenticated only
# there is a read only unless authenticated, i might consider
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': config('PAGESIZE', default=5, cast=int),
}

# this works for gmail
# adding ability to send email via gmail
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='notARealUser@gmail.com')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='Tot@lyF@k3P@$$w0rd')

# this works for my web host
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'imap.benspelledabc.me'
EMAIL_USE_TLS = False
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='notARealUser@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='Tot@lyF@k3P@$$w0rd')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


CRISPY_TEMPLATE_PACK = 'bootstrap4'

DJANGO_LOG_LEVEL = DEBUG
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '{"asctime":"%(asctime)s", "name":"%(name)s", "function":"%('
                      'funcName)s", "level":"%(levelname)s", "message":"%(message)s"} '

        },
        'file': {
            'format': '{"asctime":"%(asctime)s", "name":"%(name)s", "function":"%(funcName)s", '
                      '"level":"%(levelname)s", "message":"%(message)s"} '
        }
    },
    'handlers': {
        'console': {
            'level': 'WARN',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'WARN',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(BASE_DIR, 'data/django3.log')
        }
    },
    'loggers': {
        '': {
            'level': 'WARN',
            'handlers': ['console', 'file']
        }
    }
}

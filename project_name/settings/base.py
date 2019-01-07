"""
Base Django settings for {{ project_name }}. These settings are common across all environments

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

import os
import dj_database_url

from django.utils.crypto import get_random_string

from .env import env

DEBUG = False

ALLOWED_HOSTS = ['*']
PROJECT_NAME = '{{ project_name }}'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# You'll want to set this to your Agency name
AGENCY       = PROJECT_NAME

DATABASES = {}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'uaa_client.middleware.UaaRefreshMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'

SECRET_KEY = env.get_credential('DJANGO_SECRET_KEY', get_random_string(50))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.contrib.messages.context_processors.messages',
                '{{ project_name }}.context_processors.site_processor'
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# CF-Django-UAA config (cg-django-uaa.readthedocs.io)
UAA_APPROVED_DOMAINS = {}
UAA_CLIENT_ID = env.get_credential('UAA_CLIENT_ID', None)
UAA_CLIENT_SECRET = env.get_credential('UAA_CLIENT_SECRET', None)
UAA_AUTH_URL = 'https://login.fr.cloud.gov/oauth/authorize'
UAA_TOKEN_URL = 'https://uaa.fr.cloud.gov/oauth/token'
UAA_LOGOUT_URL = 'https://login.fr.cloud.gov/logout.do'

#AUTO_LOGOUT_DELAY_MINUTES = 60


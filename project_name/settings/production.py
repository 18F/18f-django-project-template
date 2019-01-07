from .base import *

SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

DATABASES['default'] = dj_database_url.config(
    default='postgres://{{ project_name }}:{{ project_name }}@localhost/{{ project_name }}'
)

LOGGING = {}


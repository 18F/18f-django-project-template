from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INTERNAL_IPS = [
    '127.0.0.1'
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]

UAA_CLIENT_ID = 'testtesttesttesttesttesttesttesttesttesttest'
UAA_CLIENT_SECRET = 'testtesttesttesttesttesttesttesttesttest'
UAA_AUTH_URL = 'fake:'
UAA_TOKEN_URL = 'fake:'
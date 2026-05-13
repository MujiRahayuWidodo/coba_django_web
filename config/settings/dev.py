from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Tambahkan apps untuk development jika diperlukan
INSTALLED_APPS += [
    'debug_toolbar',
    'schema_graph',
]

MIDDLEWARE += [
    'django_debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
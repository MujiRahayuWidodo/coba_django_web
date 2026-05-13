from .base import *

DEBUG = False
ALLOWED_HOSTS = []  # Isi dengan domain production nanti

# Database production (contoh PostgreSQL)
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         ...
#     }
# }
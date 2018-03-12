from .base import *

DEBUG = True
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.dev.application'
INSTALLED_APPS += [
    'django_extensions',
]

# Database
secrets = json.loads(open(SECRETS_DEV, 'rt').read())
# DATABASES = secrets['DATABASES']
set_config(secrets, module_name=__name__, start=True)

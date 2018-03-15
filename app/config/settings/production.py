from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.elasticbeanstalk.com',
]
WSGI_APPLICATION = 'config.wsgi.production.application'
INSTALLED_APPS += [
    'storages',
]

# Database
secrets = json.loads(open(SECRETS_PRODUCTION, 'rt').read())
# DATABASES = secrets['DATABASES']
set_config(secrets, module_name=__name__, start=True)

# Media(User-uploaded files)를 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFilesStorage'
# Static files(collectstatic)을 위한 스토리지
# STATICFILES_STORAGE = 'config.storage.StaticFilesStorage'

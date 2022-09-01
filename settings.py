ALLOWED_HOSTS = [
  '192.168.1.30',
  'localhost',
  'etc',
]

# Static files require
INSTALLED_APPS = [
  'django.contrib.staticfiles',
]

# SQL Database
DATABASES = {
  'default': {
    'ENGINE': 'mssql',
    'NAME': 'SequelDB',
    'USER': 'myUser',
    'PASSWORD': 'mySecretPass',
    'HOST': '192.168.1.29',
    'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server'},
  }
}

# More Static implements
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads/')
MEDIA_URL = '/uploads/'

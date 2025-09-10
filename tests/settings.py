import os


SECRET_KEY = '!fake'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'toconline',
    'tests'
]

DATABASES = {
    'default': {
        'NAME': ':memory:',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

TOCONLINE_BASE_URL = os.getenv('TOCONLINE_BASE_URL')  # https://app<N>.toconline.pt
TOCONLINE_OAUTH_CLIENT_ID = os.getenv('TOCONLINE_OAUTH_CLIENT_ID')
TOCONLINE_OAUTH_CLIENT_SECRET = os.getenv('TOCONLINE_OAUTH_CLIENT_SECRET')
TOCONLINE_OAUTH_REDIRECT_URI = os.getenv('TOCONLINE_OAUTH_REDIRECT_URI')

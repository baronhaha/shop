DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'golden',
        'PASSWORD': 'qop000qop',
        'HOST': 'localhost',
        'PORT': '',
    }
}
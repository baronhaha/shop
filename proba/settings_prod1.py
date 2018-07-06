DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'gold',
        'PASSWORD': 'qop000qop',
        'HOST': 'localhost',
        'PORT': '',
    }
}
SOCIAL_AUTH_POSTGRES_JSONFIELD = True
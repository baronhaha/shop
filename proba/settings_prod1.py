DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'gold',
        'PASSWORD': 'qopgoldqop',
        'HOST': 'localhost',
        'PORT': '',
    }
}
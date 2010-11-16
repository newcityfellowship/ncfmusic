from host_settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jcalvinward_ncfmusic',                      # Or path to database file if using sqlite3.
        'USER': 'jcalvinward_ncfmusic',                      # Not used with sqlite3.
        'PASSWORD': 'ZZGLUQASRdCZMvsYtHzh',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}





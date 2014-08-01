from host_settings.common import *
import datetime

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ncfmusic',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '/Users/ben/mdk/ncfmusic/ncfmusic.db',                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

INSTALLED_APPS = (
    'grappelli',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'ncfmusic.apps.content',
    'ncfmusic.apps.heroshots',
    'debug_toolbar',
    'filebrowser',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    #     'LOCATION': 'cache_table',
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

PAYPAL_API_USERNAME = 'benthu_1358887459_biz_api1.gmail.com'
PAYPAL_API_PASSWORD = '1358887479'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AbAqRq085Xvb27QCS7PSd7fcLMTd'

PAYPAL_API_ENDPOINT = 'https://api-3t.sandbox.paypal.com/nvp'   # Sandbox URL, not production
PAYPAL_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr&cmd=_express-checkout&token='

PAYPAL_RETURNURL = 'http://localhost:8000/paypal-return/'
PAYPAL_CANCELURL = 'http://localhost:8000/paypal-cancel/'

CONFERENCE_COSTS = {
    'single': 75,
    'early': 50,
    'group': 50,
    'student': 30
}

CONFERENCE_EARLY_DEADLINE = datetime.date(2013, 7, 1)

#Buyer
#benthu_1341257872_per@gmail.com
#358890238

#benthu_1359341446_per@gmail.com
#359341486

#benthu_1358887459_biz@gmail.com
#358887374

TWITTER_CONSUMER_KEY = '3PJ40NLVkQrswbWWuJtrHx4Dx'
TWITTER_CONSUMER_SECRET = '5xkUmvqlPRodjyqxuy02Yu0WtlGe4rIalqGz9PIniBYOunfJKz'
TWITTER_ACCESS_TOKEN_KEY = '22872565-UowrVz5qTFWvrVvSfxfDqEj2cgA8REMMXOM5yvEb3'
TWITTER_ACCESS_TOKEN_SECRET = 'TkEvcVTFkQAIXxPhE1jXIcjrJ3NqO8JymXWuxOKbkmvCj'

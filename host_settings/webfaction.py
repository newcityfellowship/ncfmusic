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

PAYPAL_API_USERNAME = 'paypal_api1.newcityfellowship.com'
PAYPAL_API_PASSWORD = 'JGFXEPBBRUXJWB39'
PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31As4PZj2q0fBXwAR3Tr-4oFIcKjWs'


PAYPAL_API_ENDPOINT = 'https://api-3t.paypal.com/nvp'   
PAYPAL_URL = 'https://www.paypal.com/cgi-bin/webscr&cmd=_express-checkout&token='

# PAYPAL_RETURNURL = 'http://ncfmusic.com/paypal-return/'
# PAYPAL_CANCELURL = 'http://ncfmusic.com/paypal-cancel/'




# PAYPAL_API_USERNAME = 'benthu_1358887459_biz_api1.gmail.com'
# PAYPAL_API_PASSWORD = '1358887479'
# PAYPAL_API_SIGNATURE = 'AFcWxV21C7fd0v3bYYYRCpSSRl31AbAqRq085Xvb27QCS7PSd7fcLMTd'

# PAYPAL_API_ENDPOINT = 'https://api-3t.sandbox.paypal.com/nvp'   # Sandbox URL, not production
# PAYPAL_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr&cmd=_express-checkout&token='

PAYPAL_RETURNURL = 'http://ncfmusic.com/paypal-return/'
PAYPAL_CANCELURL = 'http://ncfmusic.com/paypal-cancel/'

CONFERENCE_COST = 20

TWITTER_CONSUMER_KEY = 'qcwBy1j09P6yTtK2NH0atF5Nn'
TWITTER_CONSUMER_SECRET = 'swxvAQpTaLAuMHWDKr9eIpfSw30jDnITfuQh4jyh0fRJUML82W'
TWITTER_ACCESS_TOKEN_KEY = '624055010-JZKjjwKSZItHxSE5QdGVGk9E56yx9vNK50hxkwQV'
TWITTER_ACCESS_TOKEN_SECRET = 'x9monXjfpSM1sXUnWK1lJwvdQPJCPGylaWWU4EKE3Js3o'


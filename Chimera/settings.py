from databases import databases
import os


PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

DEBUG = False

ADMINS = (
    ('Michael', 'michael@mealsloth.com'),
)

MANAGERS = ADMINS

DATABASES = databases()

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'api.mealsloth.com']

SECRET_KEY = '$cl98j&&uh&h5$)zrj(mp62)-$(thx%r4+phj_fh(za6g0al!u'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Chimera.urls'

WSGI_APPLICATION = 'Chimera.wsgi.app'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'Chimera',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Google Cloud Storage

GCS_CLIENT_ID = 'mealsloth-chimera-ap01-cloudstorage-bu01'

GCS_CLIENT_KEY = 'GOOG257P2OBJ6JUKAPST'

GCS_CLIENT_SECRET = '3i8tSK69upv1aWEW0tCxBwj0/HST0/ladjxNpjG8'

# LIBCLOUD_PROVIDERS = {
#     'google': {
#         'type': 'libcloud.storage.types.Provider.GOOGLE_STORAGE',
#         'user': 'mealsloth-chimera-ap01',
#         'key': GCS_CLIENT_KEY,
#         'bucket': GCS_CLIENT_ID,
#     }
# }

GOOGLE_CLOUD_STORAGE_BUCKET = '/' + GCS_CLIENT_ID
GOOGLE_CLOUD_STORAGE_URL = 'http://storage.googleapis.com/' + GCS_CLIENT_ID
GOOGLE_CLOUD_STORAGE_DEFAULT_CACHE_CONTROL = 'public, max-age: 7200'

DEFAULT_FILE_STORAGE = 'google.storage.google_cloud.GoogleCloudStorage'

# OAuth 2.0

OAUTH_CLIENT_ID = '265360872473-2hhoa60jmo32flkfn4pbaf5og138gc9s.apps.googleusercontent.com'
OAUTH_CLIENT_SECRET = '58qDd-7TqjKbIF7jKb6KTPm4'

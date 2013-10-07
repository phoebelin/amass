# Django settings for amass project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dominick Ng', 'dominick.ng@gmail.com'),
    ('Yang Wang', 'azznrivera@gmail.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_(e*$i0ulk6#un_7x-qy_-((j19$w3#1ash&amp;329=6x#7*!m+9b'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'postman.context_processors.inbox',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'amass.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'amass.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'crispy_forms',
    'postman',
    'ajax_select',
    'longerusername',
    'debug_toolbar',
    'amass.common',
    'amass.videos',
    'amass.equipment',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django_extensions',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

CRISPY_TEMPLATE_PACK = 'bootstrap'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_SHOW_USER_AS = 'get_full_name'

POSTMAN_AUTOCOMPLETER_APP = {
    'name': 'ajax_select',
    'field': 'AutoCompleteField',
    'arg_name': 'channel',
    'arg_default': 'user', # no default, mandatory to enable the feature
}

POSTMAN_MAILER_APP = 'mailer'

AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'
AJAX_LOOKUP_CHANNELS = {
    'user'  : {'model': 'auth.user', 'search_field': 'first_name'}
}

AUTH_PROFILE_MODULE = 'amass.common.UserProfile'

INTERNAL_IPS = ('127.0.0.1',)

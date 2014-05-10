# Django settings for farmjango project.
import os
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.split(PROJECT_PATH)[0]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

STATIC_URL = '/media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "media"),
)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dm195c_n(qv4!x-o7!5akh$q19vvrw$o6@2p_&^e(()qi6zojl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'web.misc.middleware.Middleware',
    # 'django.middleware.transaction.TransactionMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + '/templates',
)

INSTALLED_APPS = [
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.syndication',
    'django.contrib.staticfiles',
    'django.contrib.messages',

    'south',

    'web.api',
    'web.comments',
    'countryinfo',
    'data',
    'search',
    'feeds',
    'frontend',
    'misc',
    'pagination',
    'tagging',
    'registration',
    'profiles',
    'treebeard',
    'haystack',
    'listmaker',
    'features',
    'typogrify',
    'piston',
    'indexer',
    'paging',
    'petition',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    "django.core.context_processors.request",
    'data.context_processors.country',
    # 'data.context_processors.ip_country',
    # 'listmaker.context_processors.list_items',
    'misc.context_processors.google_api_key',
    'misc.context_processors.header_class',
    'data.context_processors.breadcrumb',
    'data.context_processors.data_totals_info',
    'features.context_processors.featured_items',
)

ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = '/login/'
AUTH_PROFILE_MODULE = "misc.Profile"
DEFAULT_FROM_EMAIL = "team@farmsubsidy.org"

DEFAULT_CHARSET = "utf8"

INTERNAL_IPS = ('127.0.0.1',)

COMMENTS_APP = 'web.comments'

EMAIL_PORT = 1025

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    }
}

LATEST_YEAR = 2013
STATS_YEAR = 2008
STATS_DIR = ROOT_PATH + '/data/stats'

CACHE_BACKEND = 'redis_cache.cache://localhost:6379'
CACHE_MIDDLEWARE_KEY_PREFIX = 'farm'


PISTON_DISPLAY_ERRORS = False


QUEUE_BACKEND = 'redisd'
QUEUE_REDIS_CONNECTION = 'localhost:6379'
QUEUE_REDIS_DB = 0

DATE_FORMAT = 'j F Y'


FILE_CACHE_PATH = ROOT_PATH + "/data/cache"

# GHEAT_ALWAYS_BUILD = False
GHEAT_FILESYSTEM_STORAGE_DIR = STATIC_ROOT + "heatmap/tiles/"
GHEAT_BUILD_EMPTIES = False
GHEAT_STORAGE_BACKEND = 1

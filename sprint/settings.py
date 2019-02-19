"""
Django settings for sprint project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import shutil

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2x%e6otzp$0tcc^$=2-25ypgn&%34)d1pqv^++99n^mx4srigz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'account.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'account',
    'homepage',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sprint.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            # see the DMP documentation, "configuration options" page for available options
            'CONTENT_PROVIDERS': [
                            {   'provider': 'django_mako_plus.JsContextProvider' },
                            {   'provider': 'django_mako_plus.CompileScssProvider',
                                'sourcepath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss'),
                                'targetpath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss.css'),
                                # if you need to override the default command:
                                # 'command': lambda p: [ 'sass', f'--load-path="{BASE_DIR}"', p.sourcepath, p.targetpath ],
                            },
                            {   'provider': 'django_mako_plus.CssLinkProvider',
                                'filepath': lambda p: os.path.join(p.app_config.name, 'styles', p.template_relpath + '.scss.css'),
                            },
                            {   'provider': 'django_mako_plus.JsLinkProvider' },
                        ],
        },

    },
    {
        'NAME': 'django',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sprint.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fomo',
        'USER': 'justi',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# A logger for DMP
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG  # SECURITY WARNING: never set this True on a live site
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django_mako_plus_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'django_mako_plus_console':{
            'class':'logging.StreamHandler',
            'formatter': 'django_mako_plus_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['django_mako_plus_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

"""
Django settings for construction project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--4w_s*(1(lo2+j71w0yz8uy!qnue&!pq=v7i5rfoe&2z%jy)ka'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False if os.environ.get('DEBUG') else True


ALLOWED_HOSTS = ['*']


# Application definition

BEFORE_APPS = [
    'jet.dashboard',
    'jet',
]

DJANGO_DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

PROJECT_APPS = [ 
    'core.apps.CoreConfig',
]

AFTER_APPS = [
    'ckeditor',
    'widget_tweaks',
    'modeltranslation',
    'rosetta'
]

INSTALLED_APPS = BEFORE_APPS + DJANGO_DEFAULT_APPS + PROJECT_APPS + AFTER_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'construction.middleware.force_default_middleware.force_default_language_middleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'construction.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.context_processors.base_html_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'construction.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("POSTGRES_DB", "construction_db"),
            "USER": os.environ.get("POSTGRES_USER", "construction_user"),
            "PASSWORD": os.environ.get(
                "POSTGRES_PASSWORD", "QOXlBsplLc52AhJrKHPJXYEw5JKNLffeQEbehaJ3"
            ),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", "5436"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ.get("POSTGRES_DB", "prod_construction_db"),
            "USER": os.environ.get("POSTGRES_USER", "prod_construction_user"),
            "PASSWORD": os.environ.get(
                "POSTGRES_PASSWORD", "QOXlBsplLc52AhJrKHPJXYEw5JKNLffeQEbehaJ3"
            ),
            "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
            "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

from django.utils.translation import ugettext_lazy
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGES = (
    ('az', ugettext_lazy('Azerbaijani')),
    ('en', ugettext_lazy('English')),
)

LANGUAGE_CODE = 'az'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'
MODELTRANSLATION_LANGUAGES = ('az', 'en')

# Rosetta settings
ROSETTA_MESSAGES_PER_PAGE = 15
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'az'
ROSETTA_SHOW_AT_ADMIN_PANEL = True

# for Field Lookup Popup
X_FRAME_OPTIONS = 'SAMEORIGIN'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

if DEBUG:
    # for collectstatic comment this line
    STATICFILES_DIRS = [BASE_DIR / 'static']
    
    # for collectstatic uncomment this line  
    # STATIC_ROOT = BASE_DIR / 'static'
else:
    STATIC_ROOT = BASE_DIR / 'static'
    

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'ckeditor/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'NumberedList', 'BulletedList', 'Link', 'Unlink']},
            {'name': 'youcustomtools', 'items': [
                    # put the name of your editor.ui.addButton here
                    'Preview',
                    'Maximize',
                ]},
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        'height': 112,
        'width': '100%',
        'tabSpaces': 4,
        'toolbarLocation': 'top',
        'removePlugins': 'elementspath',
        'resize_enabled': False,
        'extraPlugins': ','.join([
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}

################EMAIL CONFIG######################

DEFAULT_FROM_EMAIL = 'yasharface@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'cavidan.hasanli98@gmail.com'
EMAIL_HOST_PASSWORD = 'q1w2e3cvdn'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

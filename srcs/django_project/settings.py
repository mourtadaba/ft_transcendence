"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 5.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print(f"BASE_DIR: {BASE_DIR}")
print(f"TEMPLATES DIRS: {[BASE_DIR / 'templates']}")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'django-insecure-ge&!bzmr=3ows=fk$(m5o(iz1o*#$+$*81&ep99r!(1z=abbl^'
FT_CLIENT_ID = 'u-s4t2ud-b855b6816874401e5044c60fa9f6f223acc039deaf9853f85d6a0a57679c7723'
FT_CLIENT_SECRET = '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'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'True'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'channels',
    'daphne',

    'chat.apps.ChatConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'authentification'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home"

LOGOUT_REDIRECT_URL = "home"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


AUTH_USER_MODEL = 'authentification.User'
# URL de redirection vers l'autorisation 42
AUTHORIZE_URL = 'https://api.intra.42.fr/oauth/authorize'
TOKEN_URL = 'https://api.intra.42.fr/oauth/token'
FT_REDIRECT_URI = 'http://localhost:8000/callback'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Ajoutez ici d'autres backends si nécessaire
]

# Channels
ASGI_APPLICATION = 'django_project.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
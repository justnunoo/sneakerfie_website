"""
Django settings for sneakerfie project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zlxwfv5ra+bnr7j!zif)okp6&7#c79ty=-=e@xwk2+fv!#5ty('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shoe_items',
    'chat',
    'channels',
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    'crispy_forms',
    "crispy_bootstrap4",
    
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {'access_type': 'online'},
    }, 
    # 'APP': {
    #         'client_id': '118965752580-vvb9oklai2mgil32smlmrdl3923o043e.apps.googleusercontent.com',
    #         'secret': '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',
    #         'key': ''
    #     }
    }


AUTHENTICATION_BACKENDS = [
    # Default backend for Django authentication.
    'django.contrib.auth.backends.ModelBackend',

    # Allauth specific authentication methods, such as login by e-mail.
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True

# or 'mandatory' if you want email verification
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  

# LOGIN_REDIRECT_URL :- destination of login page in your urls.py
LOGIN_REDIRECT_URL = '/'
# ACCOUNT_LOGOUT_REDIRECT :- where to redirect when user logout
ACCOUNT_LOGOUT_REDIRECT = '/'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
]

ROOT_URLCONF = 'sneakerfie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shoe_items.context_processors.cart_item_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'sneakerfie.wsgi.application'

DOMAIN = "sneakerfie.com"

SITE_ID=1
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

TIME_ZONE = 'GMT'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'static', 'nike'),
    os.path.join(BASE_DIR, 'static', 'adidas'),
    os.path.join(BASE_DIR, 'static', 'puma'),
    os.path.join(BASE_DIR, 'static', 'jordan'),
    os.path.join(BASE_DIR, 'static', 'vans'),
    os.path.join(BASE_DIR, 'static', 'puma'),
    os.path.join(BASE_DIR,'static', 'reebok'),
    os.path.join(BASE_DIR,'static', 'new_balance'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#setting for crispy bootstrap
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

#settings for sinple message transfer protocol
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'justnunoo1@gmail.com'
EMAIL_HOST_PASSWORD = 'objy wazf umqw amii'


django_heroku.settings(locals())

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
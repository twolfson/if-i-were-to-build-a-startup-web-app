"""
Django settings for project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

ENV = os.environ.get("ENV", "development")
DEVELOPMENT = "development"
TEST = "test"
PRODUCTION = "production"
assert ENV in (DEVELOPMENT, TEST, PRODUCTION)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-secret-key"
assert ENV != PRODUCTION, "SECRET_KEY not configured for production"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV == DEVELOPMENT


ALLOWED_HOSTS = []
assert ENV != PRODUCTION, "ALLOWED_HOSTS not configured for production"


# Application definition

INSTALLED_APPS = [
    "api.apps.ApiConfig",
    "authn.apps.AuthNConfig",
    # Default apps from Django
    "django.contrib.admin",
    # Already present by default, but also required by django-allauth, https://docs.allauth.org/en/latest/installation/quickstart.html  # noqa:E501
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    # Already present by default, but also required by django-allauth, https://docs.allauth.org/en/latest/installation/quickstart.html  # noqa:E501
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Used for shell_plus and runserver_plus
    "django_extensions",
    # allauth-ui + widget tweaks (custom default template), required before `allauth`, https://github.com/danihodovic/django-allauth-ui/tree/05cfec03ba9560f5fbec4c6cdd10ce80fdcc5dae#installation  # noqa:E501
    "allauth_ui",
    "widget_tweaks",
    # https://docs.allauth.org/en/latest/installation/quickstart.html  # noqa:E501
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    # https://github.com/skorokithakis/django-loginas/tree/v0.3.11#installing-django-loginas
    "loginas",
    # Social providers (e.g. GitHub, Google) can be found here: https://docs.allauth.org/en/latest/installation/quickstart.html  # noqa:E501
    # Nothing set up yet
    # https://www.django-rest-framework.org/
    "rest_framework",
]
# https://github.com/danihodovic/django-allauth-ui/tree/05cfec03ba9560f5fbec4c6cdd10ce80fdcc5dae#installation
assert ENV != PRODUCTION, "allauth_ui requires `collectstatic` for production, please verify that's been added"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # https://docs.allauth.org/en/latest/installation/quickstart.html
    "allauth.account.middleware.AccountMiddleware",
    # Handle setting a logged_in cookie after every other request
    "authn.middleware.logged_in_cookie_middleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Required by `allauth`, https://docs.allauth.org/en/latest/installation/quickstart.html
                "django.template.context_processors.request",
            ],
        },
    },
]

# In Django 4.2, cached template loading is enabled in all environments (frustrating)
#   This works around that, https://stackoverflow.com/a/75342761
if DEBUG:
    assert len(TEMPLATES) == 1, "Encountered unexpected TEMPLATES change"
    assert TEMPLATES[0]["APP_DIRS"], "Encountered unexpected `APP_DIRS` change"
    assert not hasattr(TEMPLATES[0]["OPTIONS"], "loaders"), "Encountered unexpected `loaders` setting"
    del TEMPLATES[0]["APP_DIRS"]
    TEMPLATES[0]["OPTIONS"]["loaders"] = [
        "django.template.loaders.filesystem.Loader",
        "django.template.loaders.app_directories.Loader",
    ]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Authentication
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    #   From https://docs.allauth.org/en/latest/installation/quickstart.html
    "django.contrib.auth.backends.ModelBackend",
    # https://docs.allauth.org/en/latest/installation/quickstart.html
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Output emails to console for development
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
assert ENV != PRODUCTION, "EMAIL_BACKEND not configured for production"


# Set up CSRF overrides due to Django/React proxy
# https://github.com/django/django/blob/4.2.6/django/conf/global_settings.py#L582
# ALLOWED_HOSTS is also valid (more properly for CORS though), https://github.com/django/django/blob/4.2.6/django/middleware/csrf.py#L332-L338  # noqa:E501
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
]
assert ENV != PRODUCTION, "CSRF_TRUSTED_ORIGINS not configured for production"
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
assert ENV != PRODUCTION, "CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE not configured for production"
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Configure Django REST Framework, https://www.django-rest-framework.org/tutorial/quickstart/#pagination
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "PAGE_SIZE": 10,
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Auth settings
#   https://docs.djangoproject.com/en/4.2/topics/auth/default/#django.contrib.auth.decorators.login_required
#   https://docs.djangoproject.com/en/4.2/ref/settings/#login-url
# DEV: Django will respect `next` despite specifying this (redirects to `?next=***` after login)
# If we don't provide this and there's no `next`, then login will redirect /accounts/profile/
# Consider logout via a POST form to be YAGNI experience, esp for a small site
ACCOUNT_LOGOUT_ON_GET = True
# Don't preserve casing as it uses `__iexact` which can be expensive,
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
LOGIN_REDIRECT_URL = "/auth-success"
LOGIN_URL = "/auth/login/"
# If we don't provide this, then logout confirmation page is in Django Admin
LOGOUT_REDIRECT_URL = "/auth/login"

# django-allauth configuration, https://docs.allauth.org/en/latest/installation/quickstart.html
SOCIALACCOUNT_PROVIDERS = {
    # When adding a new provider, follow post-installation tasks: https://docs.allauth.org/en/latest/installation/quickstart.html#post-installation  # noqa:E501
}

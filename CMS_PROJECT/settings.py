import os
from pathlib import Path
from datetime import timedelta

# -------------------------
# Base Directory
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Environment Setup
# -------------------------
# Set DJANGO_ENV to 'production' on your live server
DJANGO_ENV = os.getenv("DJANGO_ENV", "development")

# -------------------------
# Security Settings
# -------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-secret-key")

DEBUG = DJANGO_ENV == "development"

# Allowed hosts
if DEBUG:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
else:
    allowed_hosts_env = os.getenv("DJANGO_ALLOWED_HOSTS", "")
    ALLOWED_HOSTS = [host.strip() for host in allowed_hosts_env.split(",") if host.strip()]

# -------------------------
# Installed Apps
# -------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "corsheaders",

    # Your app
    "CMS_SYSTEM",
]

# -------------------------
# Middleware
# -------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Keep it near the top
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# -------------------------
# CORS (Cross-Origin)
# -------------------------
CORS_ALLOW_ALL_ORIGINS = True
# -------------------------
# URL Config
# -------------------------
ROOT_URLCONF = "CMS_PROJECT.urls"

# -------------------------
# Templates
# -------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # Make sure templates are here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # Needed for auth in templates
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------
# WSGI Application
# -------------------------
WSGI_APPLICATION = "CMS_PROJECT.wsgi.application"

# -------------------------
# Database
# -------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "cms_db"),
        "USER": os.getenv("POSTGRES_USER", "cms_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "admin@2025"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5433"),
        "OPTIONS": {
            "options": "-c search_path=public",
        },
    }
}

# -------------------------
# Password Validation
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# -------------------------
# Internationalization
# -------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Dar_es_Salaam"
USE_I18N = True
USE_L10N = True  # You were missing this; usually recommended for localization
USE_TZ = True

# -------------------------
# Static and Media Files
# -------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # For development
STATIC_ROOT = BASE_DIR / "staticfiles"    # For collectstatic in production

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------
# Django REST Framework
# -------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}

# -------------------------
# JWT Settings
# -------------------------
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# -------------------------
# Logging (Basic Setup)
# -------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "INFO",
    },
}

# -------------------------
# Default Primary Key Field
# -------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from .base import *

DEBUG = True



# =====================================
# Database
# =====================================

USE_SQLITE = env.bool("USE_SQLITE", default=False)

if USE_SQLITE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": env.db("DATABASE_URL"),
    }


# =====================================
# CORS & CSRF
# =====================================

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True

# No HTTPS locally
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Don't tell Django it's behind a proxy
SECURE_PROXY_SSL_HEADER = None


# =====================================
# Static & Media
# =====================================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Use local filesystem
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
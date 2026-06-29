from .base import *

DEBUG = False


# =====================================
# Database configuration\
# =====================================

DATABASES = {
    "default": env.db("DATABASE_URL")
}

DATABASES["default"]["CONN_MAX_AGE"] = 600
DATABASES["default"]["CONN_HEALTH_CHECKS"] = True


# =======================================
# CSFR and CORS
# =======================================

# CORS configuration
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_CREDENTIALS = True

# Trusted origins
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

# Tell Django requests came through HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Secure cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# =========================================
# Media and static files configuration
# =========================================
STATIC_BUCKET_NAME = "nonware-demo-backend-static"
MEDIA_BUCKET_NAME = "nonware-demo-backend-media"

STATIC_URL = f"https://storage.googleapis.com/{STATIC_BUCKET_NAME}/static/"
MEDIA_URL = f"https://storage.googleapis.com/{MEDIA_BUCKET_NAME}/media/"

STORAGES = {
    "default": {
        "BACKEND": "config.storage_backends.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "config.storage_backends.StaticStorage",
    },
}
from .base import *

DEBUG = True


DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="postgres://postgres:password@db:5432/nonware_db",
    )
}

CORS_ALLOW_ALL_ORIGINS = True
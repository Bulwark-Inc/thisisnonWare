import os
from config.api.router import api


@api.get("/")
def root(request):
    return {
        "status": "ok",
        "service": "backend-api"
    }


@api.get("/info")
def info(request):
    return {
        "service": "backend-api",
        "version": os.getenv("APP_VERSION", "dev"),
        "environment": os.getenv("ENVIRONMENT", "unknown"),
        "status": "running"
    }

@api.get("/health")
def health(request):
    return {
        "status": "healthy"
    }
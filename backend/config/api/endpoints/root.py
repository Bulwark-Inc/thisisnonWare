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
        "version": "v1",
        "environment": "production",
        "status": "running"
    }

@api.get("/health")
def health(request):
    return {
        "status": "healthy"
    }
from config.api.router import api


@api.get("/health")
def health(request):
    return {
        "status": "healthy"
    }
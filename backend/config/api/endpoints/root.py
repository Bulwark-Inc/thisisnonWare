from config.api.router import api


@api.get("/")
def root(request):
    return {
        "status": "ok",
        "service": "backend-api"
    }
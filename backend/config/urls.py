from django.contrib import admin
from django.urls import path

from config.api.router import api
from config.api.endpoints import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls),
]
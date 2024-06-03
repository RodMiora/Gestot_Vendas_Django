
from django.contrib import admin
from django.urls import path, include
from usuarios.views import redirect_to_login



urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", include('usuarios.urls')),
     path("", redirect_to_login),
]

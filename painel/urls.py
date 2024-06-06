
from django.contrib import admin
from django.urls import path, include
from usuarios.views import redirect_to_login



urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", include('usuarios.urls')),
    path('dashboard/', include('dashboards.urls')),
    path('clientes/', include('clientes.urls')), 
    path('produtos/', include('produtos.urls')), 
    path("", redirect_to_login),
]

# dashboards/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # Página inicial do dashboard
    path('clientes/', views.clientes, name='clientes_dashboard'),  # Página de clientes
    path('produtos/', views.produtos, name='produtos_dashboard'),  # Página de produtos
    path('logout/', views.logout_view, name='logout_dashboard'),  # URL para fazer logout
]

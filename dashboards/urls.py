from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # Página inicial do dashboard
    path('clientes/', include('clientes.urls')),  # Incluir as URLs do aplicativo Clientes
    path('produtos/', views.produtos, name='produtos_dashboard'),  # Página de produtos
    path('logout/', views.logout_view, name='logout_dashboard'),  # URL para fazer logout
    path('clientes/', views.clientes, name='clientes_dashboard'),  # URL para a página de clientes no dashboard
]

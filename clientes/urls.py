from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),  # Página inicial do aplicativo de clientes
    path('lista/', views.lista_clientes, name='lista_clientes'),  # Lista de clientes
    path('<int:id_cliente>/', views.detalhes_cliente, name='detalhes_cliente'),  # Detalhes de um cliente específico
    path('<int:id_cliente>/editar/', views.editar_cliente, name='editar_cliente'),  # Editar um cliente
]

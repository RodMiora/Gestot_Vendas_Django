# clientes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),  # Lista de clientes
    path('<int:id_cliente>/', views.detalhes_cliente, name='detalhes_cliente'),  # Detalhes de um cliente específico
    path('novo/', views.novo_cliente, name='novo_cliente'),  # Formulário para adicionar novo cliente
    path('<int:id_cliente>/editar/', views.editar_cliente, name='editar_cliente'),  # Formulário para editar cliente
    # Adicione outras URLs conforme necessário para o seu aplicativo de clientes
]

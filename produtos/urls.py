from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),            # Lista de produtos
    path('<int:id_produto>/', views.detalhes_produto, name='detalhes_produto'),  # Detalhes de um produto específico
    path('novo/', views.novo_produto, name='novo_produto'),          # Formulário para adicionar novo produto
    path('<int:id_produto>/editar/', views.editar_produto, name='editar_produto'),  # Formulário para editar produto
    path('<int:id_produto>/excluir/', views.excluir_produto, name='excluir_produto'),  # Excluir produto
]

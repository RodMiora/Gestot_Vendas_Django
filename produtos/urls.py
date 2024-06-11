from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produtos_view, name='produtos_view'),  # Nome da view deve ser 'produtos_view'
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('lista/', views.lista_produtos, name='lista_produtos'),
    path('<int:id_produto>/', views.detalhes_produto, name='detalhes_produto'),
]

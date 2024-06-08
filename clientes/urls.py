from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='clientes'),
    path('lista/', views.lista_clientes, name='lista_clientes'),
    path('<int:id_cliente>/', views.detalhes_cliente, name='detalhes_cliente'),
    path('<int:id_cliente>/editar/', views.editar_cliente, name='editar_cliente'),
]

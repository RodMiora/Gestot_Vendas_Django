# dashboards/views.py

from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from clientes.models import Cliente
from datetime import datetime

@login_required
def dashboard_view(request):
    categorias = ['Categoria A', 'Categoria B', 'Categoria C']  # Exemplo de categorias
    clientes_por_categoria = [10, 20, 30]  # Exemplo de dados de clientes por categoria
    return render(request, 'dashboards/dashboard.html', {
        'username': request.user.username,
        'categorias': categorias,
        'clientes_por_categoria': clientes_por_categoria,
    })

@login_required
def clientes(request):
    return render(request, 'clientes/clientes.html')

@login_required
def produtos(request):
    return render(request, 'produtos/produtos.html')

@login_required
def logout_view(request):
    logout(request)  # type: ignore
    return redirect('/usuarios/login')

@login_required
def clientes_por_periodo(request, month):
    year = datetime.now().year  # Ano atual
    clientes = Cliente.objects.filter(data_cadastro__year=year, data_cadastro__month=month)
    dias_do_mes = {day: 0 for day in range(1, 32)}
    for cliente in clientes:
        dia = cliente.data_cadastro.day
        dias_do_mes[dia] += 1
    return JsonResponse({'clientes_por_dia': list(dias_do_mes.values())})

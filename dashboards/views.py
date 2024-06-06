# dashboards/views.py
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def dashboard_view(request):
    return render(request, 'dashboards/dashboard.html', {'username': request.user.username})

def clientes(request):
    # Lógica para a página de clientes
    return render(request, 'clientes/clientes.html')

def produtos(request):
    # Lógica para a página de produtos
    return render(request, 'produtos/produtos.html')

def logout_view(request):
    # Lógica para o logout do usuário
    logout(request) # type: ignore
    return redirect('index')  # Redireciona para a página inicial após logout
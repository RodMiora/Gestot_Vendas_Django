# clientes/views.py

from django.shortcuts import render, redirect
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required

def clientes(request):
    # Esta função foi removida porque a lógica está agora em lista_clientes
    pass

@login_required
def lista_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user  # Atribui diretamente o usuário autenticado ao cliente
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.filter(user=request.user)
    context = {
        'form': form,
        'clientes': clientes,
        'username': request.user.username
    }
    return render(request, 'clientes/clientes.html', context)

def detalhes_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    context = {
        'cliente': cliente
    }
    return render(request, 'clientes/detalhes_cliente.html', context)

def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'cliente': cliente
    }
    return render(request, 'clientes/editar_cliente.html', context)

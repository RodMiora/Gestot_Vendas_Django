# clientes/views.py

from django.shortcuts import get_object_or_404, redirect, render
from .models import Cliente  # Importe o modelo de Cliente ou o modelo relevante
from .forms import ClienteForm  # type: ignore # Importe o formulário de Cliente ou o formulário r


def lista_clientes(request):
    clientes = Cliente.objects.all()  # Exemplo: obtenha todos os clientes do banco de dados
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def detalhes_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    return render(request, 'clientes/detalhes_cliente.html', {'cliente': cliente})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redireciona para a lista de clientes após salvar
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/novo_cliente.html', {'form': form})


def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, pk=id_cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redireciona para a lista de clientes após salvar
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})


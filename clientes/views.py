from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente


@login_required
def lista_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
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


@login_required
def detalhes_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    context = {
        'cliente': cliente
    }
    return render(request, 'clientes/detalhes_cliente.html', context)

@method_decorator(login_required, name='dispatch')
class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        return Cliente.objects.filter(user=self.request.user)

@login_required
def editar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes_dashboard')  # Redireciona para a página de clientes após editar
    else:
        form = ClienteForm(instance=cliente)

    context = {
        'form': form,
        'cliente': cliente
    }
    return render(request, 'clientes/editar_cliente.html', context)

# produtos/views.py

from django.shortcuts import get_object_or_404, redirect, render
from produtos.forms import ProdutoForm
from .models import Produto  # Importe o modelo de Produto
from django.contrib.auth.decorators import login_required


@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()  # Consulta para buscar todos os produtos do banco de dados
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

@login_required
def detalhes_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    # Se precisar de mais lógica, adicione aqui
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})

@login_required
def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redireciona para a página de detalhes do novo produto ou outra página desejada
            return redirect('lista_produtos')  # Nome da URL para a lista de produtos
    else:
        form = ProdutoForm()
    
    return render(request, 'produtos/novo_produto.html', {'form': form})


@login_required
def editar_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            # Redireciona para a página de detalhes do produto ou outra página desejada
            return redirect('detalhes_produto', id_produto=id_produto)  # Nome da URL para detalhes do produto
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})


@login_required
def excluir_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    
    if request.method == 'POST':
        produto.delete()
        # Redireciona para alguma página após excluir o produto
        return redirect('lista_produtos')  # Redireciona para a lista de produtos após excluir
    
    return render(request, 'produtos/excluir_produto.html', {'produto': produto})
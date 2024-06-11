from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger(__name__)

@login_required
def produtos_view(request):
    produtos = Produto.objects.filter(user=request.user)

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.user = request.user
            produto.save()
            produtos_atualizados = list(Produto.objects.filter(user=request.user).values())
            return JsonResponse({'produtos': produtos_atualizados})
        else:
            return JsonResponse({'error': form.errors}, status=400)

    context = {
        'produtos': produtos,
        'username': request.user.username
    }
    return render(request, 'produtos/produtos.html', context)

@login_required
@csrf_exempt
def adicionar_produto(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            form = ProdutoForm(request.POST)
            if form.is_valid():
                produto = form.save(commit=False)
                produto.user = request.user  # Definindo o usuário logado
                produto.save()
                produtos_atualizados = list(Produto.objects.filter(user=request.user).values())
                return JsonResponse({'produtos': produtos_atualizados})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        except Exception as e:
            logger.error(f'Erro ao adicionar produto: {str(e)}')
            return JsonResponse({'error': 'Erro interno ao adicionar produto.'}, status=500)
    else:
        return JsonResponse({'error': 'Requisição inválida.'}, status=400)

@login_required
def lista_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.user = request.user
            produto.save()
            return redirect('produtos:lista_produtos')
    else:
        form = ProdutoForm()

    produtos = Produto.objects.filter(user=request.user)
    context = {
        'produtos': produtos,
        'form': form
    }
    return render(request, 'produtos/produtos.html', context)

@login_required
def detalhes_produto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto, user=request.user)
    context = {
        'produto': produto
    }
    return render(request, 'produtos/detalhes_produto.html', context)

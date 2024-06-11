# produtos/forms.py

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco_custo', 'valor_venda', 'categoria']

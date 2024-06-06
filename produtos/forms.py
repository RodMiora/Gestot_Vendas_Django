# produtos/forms.py

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'  # Ou liste os campos específicos que deseja incluir no formulário

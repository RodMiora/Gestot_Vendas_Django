# clientes/forms.py

from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']  # Defina os campos que deseja incluir no formulário

from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    CATEGORIAS = [
        ('eletronicos', 'Eletrônicos'),
        ('roupas', 'Roupas'),
        ('moveis', 'Móveis'),
        ('casa_utensilios', 'Casa e Utensílios'),
        ('variados', 'Variados')
    ]

    descricao = models.CharField(max_length=200)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Adicionando campo user
    
    @property
    def lucro_real(self):
        return self.valor_venda - self.preco_custo

    def __str__(self):
        return self.descricao

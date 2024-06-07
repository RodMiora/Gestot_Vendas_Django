from django.db import models
from django.contrib.auth.models import User  # Importe o modelo de usuário do Django, se aplicável

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # Relacionamento com o usuário

    def __str__(self):
        return self.nome

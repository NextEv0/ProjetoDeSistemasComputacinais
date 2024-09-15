from django.db import models
from django.contrib.auth.models import User  # Importa o modelo de usuário padrão

class AnimalEntry(models.Model):
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    idade = models.IntegerField()
    data_catalogacao = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o usuário que criou

    def __str__(self):
        return f"{self.nome} ({self.especie})"

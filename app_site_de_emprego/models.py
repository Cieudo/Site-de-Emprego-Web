from django.db import models


class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa = models.CharField(max_length=100)

    # Outros campos relevantes (localização, categoria, etc.)

    def __str__(self):
        return self.titulo

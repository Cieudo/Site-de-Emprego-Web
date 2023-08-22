from django.db import models

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa = models.CharField(max_length=100)
    # Outros campos

class Curriculo(models.Model):
    nome = models.CharField(max_length=100)
    experiencia = models.TextField()
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    # Outros campos

from django.db import models

class Vaga(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa = models.CharField(max_length=100)

    # Outros campos relevantes (localização, categoria, etc.)

    def __str__(self):
       return self.titulo 

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

class Candidato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

class Conta(models.Model):
    id = models.AutoField(primary_key=True)


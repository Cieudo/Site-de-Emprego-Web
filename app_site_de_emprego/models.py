from django.db import models

class Vaga(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
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

class CandidatoFormulario(models.Model):
    id = models.AutoField(primary_key=True)
    #candidado = models.ForeignKey(Candidato,on_delete=models.CASCADE)
    p1 = models.CharField(max_length=255) 
    p2 = models.CharField(max_length=255)
    p3 = models.CharField(max_length=255)
    p4 = models.CharField(max_length=255)
    p5 = models.CharField(max_length=255)
    p5 = models.CharField(max_length=255)
    p6 = models.CharField(max_length=255)
    p7 = models.CharField(max_length=255)
    p8 = models.CharField(max_length=255)
    p9 = models.CharField(max_length=255)
    p10 = models.CharField(max_length=255)


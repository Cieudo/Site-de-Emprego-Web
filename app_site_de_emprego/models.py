from django.db import models

# Create your models here.
class Candidato(models.Model):
    id_canditato = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255,null=False)
    email = models.EmailField(max_length=255)
    disponibilidade = models.CharField(max_length=10)
    pdf = models.BinaryField(max_length=16777216)

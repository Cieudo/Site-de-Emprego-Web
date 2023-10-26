from django.db import models

<<<<<<< HEAD

class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    empresa = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)

    # Outros campos relevantes (localização, categoria, etc.)

    def __str__(self):
       return self.titulo 

=======
>>>>>>> caee3d20d1a468baff122ba18c04a3defc8774b0
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    
class Vaga(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    localidade = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    # Outros campos relevantes (localização, categoria, etc.)

    def __str__(self):
       return self.titulo 

class Candidato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

class Conta(models.Model):
<<<<<<< HEAD
    id = models.AutoField(primary_key=True)
=======
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

>>>>>>> main

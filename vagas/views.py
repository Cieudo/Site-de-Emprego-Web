from django.shortcuts import render
from .models import Vaga  # Importe o modelo Vaga do seu arquivo models.py

def lista_vagas(request):
    vagas = Vaga.objects.all()  # Recupere todas as instâncias do modelo Vaga
    context = {
        'vagas': vagas  # Adicione as vagas ao contexto
    }
    return render(request, 'vagas/lista_vagas.html', lista_vagas())

from django.shortcuts import render, redirect
from .forms import VagaForm
from .models import Vaga
from django.shortcuts import get_object_or_404, render, redirect


def home(request):
    return render(request, 'home.html')

def home(request):
    vagas = Vaga.objects.all()  # Recupera todas as vagas cadastradas
    return render(request, 'home.html', {'vagas': vagas})

def loginuser(request):
    return render(request, 'loginuser.html')

def register(request):
    return render(request, 'register.html')

def registerempresa(request):
    return render(request, 'registerempresa.html')

def formulario_inscricao(request):
    return render(request, 'formulario_inscricao.html')


def cadastrar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = VagaForm()

    return render(request, 'cadastrar_vaga.html', {'form': form})

def pagina_sucesso(request):
    return redirect('home')

def escolha(request):
    return render(request,'escolha.html')

def excluir_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    
    if request.method == 'POST':
        vaga.delete()
        return redirect('home')  # Redirecione para a página inicial ou qualquer outra página após a exclusão
    
    return render(request, 'confirmar_exclusao.html', {'vaga': vaga})

    
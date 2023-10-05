from django.shortcuts import render, redirect
from .forms import VagaForm
from .models import Vaga
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')

def home(request):
    vagas = Vaga.objects.all()  # Recupera todas as vagas cadastradas
    return render(request, 'home.html', {'vagas': vagas})



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ja existe um usuario com esse username')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('home')


def login(request):
    if  request.method == "GET":
        return render(request, 'login.html')

    else:
          username = request.POST.get('username')
          senha = request.POST.get('senha')

          user = authenticate(username=username, password=senha)

          if user:
               return redirect('home')
          else:
                 return messages(request, 'login.html', {'error_message': 'Email ou senha inválidos'})


def loginuser(request):
    return render(request, 'loginuser.html')

def curriculo(request):
    return render(request, 'curriculo.html')

def registerempresa(request):
    return render(request, 'registerempresa.html')


def formulario_inscricao(request):
    return render(request, 'formulario_inscricao.html')

def candidato_panel(request):
    return render(request, 'candidato_panel.html')

def empresa_panel(request):
    return render(request, 'empresa_panel.html')


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


from django.shortcuts import render, redirect
from .forms import (VagaForm,CandidatoForm)
from .models import Vaga
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect



def home(request):
    vagas = Vaga.objects.all()  # Recupera todas as vagas cadastradas
    return render(request, 'home.html', {'vagas': vagas})

def loginuser(request):
    return render(request, 'loginuser.html')

def register(request):
    return render(request, 'register.html')

def registerempresa(request):
    return render(request, 'registerempresa.html')

def curriculo(request):
    return render(request, 'curriculo.html')

def escolha(request):
    return render(request,'escolha.html')

def candidato_panel(request):
    return render(request, 'candidato_panel.html')

def empresa_panel(request):
    return render(request, 'empresa_panel.html')

def logout_user(request):
    logout(request)
    return redirect('home')  # Redireciona para a página inicial após o logout


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome de usuário.')

        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.success(request, 'Cadastro realizado com sucesso!')
        user.save()

        return redirect('home')

    return render(request, 'cadastro.html')


def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            auth_login(request, user) # Usando a função auth_login para evitar conflitos
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            return render(request, 'login.html')


def formulario_inscricao(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = CandidatoForm()
    return render(request, 'formulario_inscricao.html', {'form': form})


def cadastrar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = VagaForm()

    return render(request, 'cadastrar_vaga.html', {'form': form})


def excluir_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    
    if request.method == 'POST':
        vaga.delete()
        return redirect('home')  # Redirecione para a página inicial ou qualquer outra página após a exclusão
    
    return render(request, 'confirmar_exclusao.html', {'vaga': vaga})

    
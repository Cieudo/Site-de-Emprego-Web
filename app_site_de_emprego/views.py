from django.shortcuts import render, redirect
from .forms import (VagaForm,CandidatoForm)
from .models import Vaga
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import Group


def home(request):
    vagas = Vaga.objects.all()  # Recupera todas as vagas cadastradas
    return render(request, 'home.html', {'vagas': vagas})

def register(request):
    return render(request, 'register.html')

def registerempresa(request):
    return render(request, 'registerempresa.html')

def escolha(request):
    return render(request,'escolha.html')

def candidato_panel(request):
    return render(request, 'candidato_panel.html')

def empresa_panel(request):
    return render(request, 'empresa_panel.html')

def curriculo(request):
    return render(request, 'curriculo,html')


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


def cadastro_empresa(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome de usuário.')

        user = User.objects.create_user(username=username, email=email, password=senha)

        # Adicione o usuário ao grupo Empresa
        group = Group.objects.get(name='Empresa')
        user.groups.add(group)

        user.save()

        permission = Permission.objects.get(codename='permission_cadastrar_vaga')
        group.permissions.add(permission)

        return redirect('home')

    return render(request, 'cadastro_empresa.html')

def cadastro_candidato(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome de usuário.')

        user = User.objects.create_user(username=username, email=email, password=senha)

        # Adicione o usuário ao grupo Candidato
        group = Group.objects.get(name='Candidato')
        user.groups.add(group)

        user.save()

        return redirect('home')

    return render(request, 'cadastro_candidato.html')

#Não é boa prática enfiar esse código aqui, mas...
#Código que verifica se o usuário atual é um superusuário
#Vai ser utilizado para permitir que o 'admin' veja o relatório de candidatos e ofertas
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

# Código que verifica se o usuário atual é um superusuário
# Vai ser utilizado para permitir que o 'admin' veja o relatório de candidatos e ofertas
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_superuser)
def relatorio_candidatos(request):
    candidatos = Candidato.objects.all()
    return render(request, 'relatorio_candidatos.html', {'candidatos': candidatos})

@user_passes_test(is_superuser)
def relatorio_ofertas(request):
    vagas = Vaga.objects.all()
    return render(request, 'relatorio_ofertas.html', {'vagas': vagas})
    def candidatura_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)

    if request.method == 'POST':
        form = CandidaturaForm(request.POST)
        if form.is_valid():
            candidatura = form.save(commit=False)
            candidatura.candidato = request.user.candidato  # Supondo que cada usuário Candidato tenha um perfil associado
            candidatura.save()
            return redirect('candidatura_confirmada')  # Redireciona para a página de confirmação
    else:
        form = CandidaturaForm()

    return render(request, 'candidatura_vaga.html', {'form': form, 'vaga': vaga})


def processar_candidatura(request, vaga_id):
    if request.method == 'POST':
        vaga = get_object_or_404(Vaga, id=vaga_id)

        # Verifica se o usuário está autenticado e possui um perfil de candidato
        if request.user.is_authenticated and hasattr(request.user, 'candidato'):
            candidato = request.user.candidato

            # Verifica se o candidato já se candidatou para a mesma vaga
            if Candidatura.objects.filter(vaga=vaga, candidato=candidato).exists():
                messages.error(request, 'Você já se candidatou para esta vaga anteriormente.')
                return redirect('candidatura_vaga', vaga_id=vaga_id)

            # Se não, cria a candidatura
            Candidatura.objects.create(vaga=vaga, candidato=candidato)

            # Redireciona para a página de confirmação de candidatura
            return redirect('candidatura_confirmada')
        else:
            # Trate o caso em que o usuário não possui um perfil de candidato
            return HttpResponse('Você precisa ter um perfil de candidato para se candidatar.')

    # Restante da lógica para renderizar o formulário, se necessário
    # ...

    return render(request, 'sua_template.html', context)
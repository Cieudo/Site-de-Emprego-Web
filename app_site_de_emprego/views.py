from django.shortcuts import render, redirect
from .forms import VagaForm
from .models import Vaga
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html', {'user': request.user})

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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 'home' deve ser o nome da URL da página inicial
        else:
            # Handle login falhou
            pass
    return render(request, 'login.html')


def loginuser(request):
    return render(request, 'loginuser.html')

def curriculo(request):
    return render(request, 'curriculo.html')


def registerempresa(request):
    return render(request, 'registerempresa.html')


def formulario_inscricao(request):
    return render(request, 'formulario_inscricao.html')

@login_required
def candidato_panel(request):
    # Adicione a lógica para exibir as vagas para onde o candidato mandou currículo
    return render(request, 'candidato_panel.html')

@login_required
def empresa_panel(request):
    if request.user.profile.tipo == 'empresa':
        # Adicione a lógica para exibir as vagas criadas pela empresa
        vagas = Vaga.objects.filter(empresa=request.user)
        return render(request, 'empresa_panel.html', {'vagas': vagas})
    else:
        # Caso o usuário não seja uma empresa, redirecione para a home
        return redirect('home')


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

@login_required
def excluir_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id, empresa=request.user)
    
    if request.method == 'POST':
        vaga.delete()
        messages.success(request, 'Vaga excluída com sucesso!')
        return redirect('empresa_panel')
    
    return render(request, 'confirmar_exclusao.html', {'vaga': vaga})


from django.shortcuts import render
from .models import Candidato

def home(request):
    return render(request,'home.html')

def loginuser(request):
    return render(request,'loginuser.html')

def register(request):
    return render(request,'register.html')
    
def postregister(request):
    if request.method =="POST":
        novo_candidato = Candidato()    
        novo_candidato.nome = request.POST.get('nome')
        novo_candidato.email = request.POST.get('email')
        novo_candidato.disponibilidade = request.POST.get('horarios') 
        novo_candidato.pdf = request.FILES.get('cv').read()
        novo_candidato.save()

        views.home(request)
    
    candidatos = {
        'candidados' : Candidato.object.all()
    }
    return render(request,'register.html')    

def registerempresa(request):
    return render(request,'registerempresa.html')

def ladingpage(request):
    return render(request,'ladingpage.html')
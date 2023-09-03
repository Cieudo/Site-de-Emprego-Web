from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def loginuser(request):
    return render(request,'loginuser.html')

def register(request):
    return render(request,'register.html')

def registerempresa(request):
    return render(request,'registerempresa.html')
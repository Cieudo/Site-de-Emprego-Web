from django.urls import path
from app_site_de_emprego import views

urlpatterns = [
    path('', views.home, name='home'),  # URL raiz correspondendo à função home
    path('loginusers/', views.loginuser, name='loginuser'),# URL para a função loginuser com "s"
    path('register/', views.register, name='register'),
    path('registerempresa/', views.registerempresa, name='registerempresa'),
    path('ladingpage/', views.ladingpage, name='ladingpage'),
]

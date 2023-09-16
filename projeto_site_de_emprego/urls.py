from django.urls import path
from app_site_de_emprego import views

urlpatterns = [
    path('', views.home, name='home'),  # URL raiz correspondendo à função home
    path('loginusers/', views.loginuser, name='loginuser'),# URL para a função loginuser com "s"
    path('register/', views.register, name='register'),
    path('registerempresa/', views.registerempresa, name='registerempresa'),
    path('escolha/', views.escolha, name='escolha'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('pagina_sucesso/', views.pagina_sucesso, name='pagina_sucesso'),
]

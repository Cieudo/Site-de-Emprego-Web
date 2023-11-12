from django.contrib import admin
from django.urls import path
from app_site_de_emprego import views

urlpatterns = [
    path('', views.home, name='home'), # URL raiz correspondendo à função home
    path('admin/', admin.site.urls), # URL para a função loginuser com "s"
    #path('loginusers/', views.loginuser, name='loginuser'),
    path('login/', views.login_user, name='login_user'),
    path('logout/',views.logout_user,name='logout_user'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('registerempresa/', views.registerempresa, name='registerempresa'),
    path('escolha/', views.escolha, name='escolha'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('excluir_vaga/<int:vaga_id>/', views.excluir_vaga, name='excluir_vaga'),
    path('formulario/', views.formulario_inscricao, name='formulario_inscricao'),
    path('candidato/', views.candidato_panel, name='candidato_panel'),
    path('empresa/', views.empresa_panel, name='empresa_panel'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('relatorio/candidatos/', views.relatorio_candidatos, name='relatorio_candidatos'),
    path('relatorio/ofertas/', views.relatorio_ofertas, name='relatorio_ofertas'),
]

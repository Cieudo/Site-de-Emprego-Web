from django.contrib import admin
from django.urls import path
from app_site_de_emprego import views
from app_site_de_emprego.views import cadastro_empresa, cadastro_candidato, candidatura_confirmada, candidatura_vaga


urlpatterns = [
    path('', views.home, name='home'), # URL raiz correspondendo à função home
    path('admin/', admin.site.urls), # URL para a função loginuser com "s"
    #path('loginusers/', views.loginuser, name='loginuser'),
    path('login/', views.login_user, name='login_user'),
    path('escolha_login/', views.escolha_login, name='escolha_login'),
    path('login_empresa/', views.login_empresa, name='login_empresa'),
    path('logout/',views.logout_user,name='logout_user'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('register/', views.register, name='register'),
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
    path('cadastro_empresa/', cadastro_empresa, name='cadastro_empresa'),
    path('cadastro_candidato/', cadastro_candidato, name='cadastro_candidato'),
    path('processar_candidatura/<int:vaga_id>/', views.processar_candidatura, name='processar_candidatura'),
    path('candidatura_vaga/<int:vaga_id>/', candidatura_vaga, name='candidatura_vaga'),
    path('candidatura_confirmada/', candidatura_confirmada, name='candidatura_confirmada'),
]
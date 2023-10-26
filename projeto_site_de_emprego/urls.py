from django.contrib import admin
from django.urls import path
from app_site_de_emprego import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('loginusers/', views.loginuser, name='loginuser'),
    path('login/', views.login, name='login'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('registerempresa/', views.registerempresa, name='registerempresa'),
    path('escolha/', views.escolha, name='escolha'),
    path('cadastrar_vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),
    path('excluir_vaga/<int:vaga_id>/', views.excluir_vaga, name='excluir_vaga'),
    path('formulario/', views.formulario_inscricao, name='formulario_inscricao'),
    path('pagina_sucesso/', views.pagina_sucesso, name='pagina_sucesso'),
    path('candidato/', views.candidato_panel, name='candidato_panel'),
    path('empresa/', views.empresa_panel, name='empresa_panel'),
    path('cadastro/', views.cadastro, name='cadastro'),
]

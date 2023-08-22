from django.urls import path
from . import views

urlpatterns = [
    path('vagas/', views.lista_vagas, name='lista_vagas'),
    path('vagas/<int:vaga_id>/', views.detalhes_vaga, name='detalhes_vaga'),
    path('curriculo/<int:vaga_id>/', views.cadastrar_curriculo, name='cadastrar_curriculo'),
]

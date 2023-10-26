<<<<<<< HEAD
from django import forms
from .models import Vaga

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'empresa']
        # Adicione outros campos conforme necessário
=======
from django import forms
from .models import (Vaga,CandidatoFormulario)

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'empresa']
        # Adicione outros campos conforme necessário

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = CandidatoFormulario
        fields = ['p1','p2','p3','p4','p5','p6','p7','p8','p9','p10']
>>>>>>> main

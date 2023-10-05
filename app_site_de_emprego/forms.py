from django import forms
from .models import Vaga

class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'empresa']
        # Adicione outros campos conforme necessário

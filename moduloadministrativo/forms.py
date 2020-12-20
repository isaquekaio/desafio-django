from django import forms
from moduloadministrativo.models import *

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['nome', 'cnes', 'cnpj', 'uf', 'municipio']

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'estoque']
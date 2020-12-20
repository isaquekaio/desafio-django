from django import forms
from moduloadministrativo.models import *

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['nome', 'cnes', 'cnpj', 'uf', 'municipio']

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'ml', 'fabricante']

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['user','data_nascimento','cns','cpf','rg','orgao_expeditor','estabelecimentos']
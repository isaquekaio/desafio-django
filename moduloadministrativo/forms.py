from django import forms
from moduloadministrativo.models import *

class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = ['nome', 'cnes', 'cnpj', 'uf', 'municipio']

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['nome']

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['lote', 'movimento']

class EstoqueItemForm(forms.ModelForm):
    class Meta:
        model = EstoqueItem
        fields = ['qtd', 'saldo', 'estoque', 'vacina']

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'ml', 'fabricante']

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['user','data_nascimento','cns','cpf','rg','orgao_expeditor','estabelecimentos']

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ['user','data_nascimento','cpf']


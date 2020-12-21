from django import forms
from django.db import transaction

from moduloadministrativo.models import *
from django.contrib.auth.forms import UserCreationForm

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
        fields = ['nota_fiscal', 'movimento']

class EstoqueItemForm(forms.ModelForm):
    class Meta:
        model = EstoqueItem
        fields = ['qtd', 'saldo', 'estoque', 'vacina']

class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome', 'ml', 'lote','fabricante']

class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = ['user','data_nascimento','cns','cpf','rg','orgao_expeditor','estabelecimentos']

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ['user','data_nascimento','cpf']

# Cadastro do usuario
class ProfissionalSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_profissional = True
        if commit:
            user.save()
        return user

class CoordenadorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_coordenador = True
        user.save()
        return user
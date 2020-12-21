from django import forms
from modulocartaovacina.models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['user','cpf','data_nascimento']

class CartaoVacinaForm(forms.ModelForm):
    class Meta:
        model = CartaoVacina
        fields = ['paciente','data','vacina','estabelecimento','profissional']
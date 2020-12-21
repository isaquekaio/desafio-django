from django import forms
from moduloagendamento.models import *

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['vacina','uf','municipio','estabelecimento','data','paciente']

class FilaAtendimentoForm(forms.ModelForm):
    class Meta:
        model = FilaAtendimento
        fields = ['status','agenda','observacao']
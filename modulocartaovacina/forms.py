from django import forms
from modulocartaovacina.models import *
from django.contrib.auth.forms import UserCreationForm

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['user','cpf','data_nascimento']

class CartaoVacinaForm(forms.ModelForm):
    class Meta:
        model = CartaoVacina
        fields = ['paciente','data','vacina','estabelecimento','profissional']

# Usuario Paciente
class PacienteSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_paciente = True
        if commit:
            user.save()
        return user
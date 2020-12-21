from django.contrib.auth.models import AbstractUser
from pessoa.models import User
from django.db import models
from moduloadministrativo.models import *

# Create your models here.
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cpf = models.CharField('CPF',max_length=11)
    data_nascimento = models.DateField('Data de Nascimento')

    class Meta:
        ordering = ['user']

    def __str__(self):
        return self.user.username

class CartaoVacina(models.Model):
    data = models.DateField('Data da Vacinação')
    vacina = models.ForeignKey(Vacina, on_delete=models.RESTRICT)
    profissional = models.ForeignKey(Profissional, on_delete=models.RESTRICT)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.RESTRICT)
    paciente = models.ForeignKey(Paciente, on_delete=models.RESTRICT)
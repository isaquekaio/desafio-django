from django.contrib.auth.models import AbstractUser
from pessoa.models import User
from django.db import models

# Create your models here.
class Uf(models.Model):
    nome = models.CharField('UF', max_length=100, blank=False)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.nome

class Municipio(models.Model):
    nome = models.CharField('UF', max_length=100, blank=False)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Estabelecimento(models.Model):
    nome = models.CharField('UF', max_length=200, blank=False)
    cnes = models.CharField('CNES', max_length=45, blank=False)
    cnpj = models.CharField('CNPJ', max_length=14, blank=False)
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return "%s - %s - %s" % (self.nome, self.cnes, self.cnpj)

class Profissional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    data_nascimento = models.DateField('Data de Nascimento')
    cns = models.CharField('CNS' ,max_length=45)
    cpf = models.CharField('CPF',max_length=11)
    rg = models.CharField('RG', max_length=12)
    orgao_expeditor = models.CharField('Orgao Expeditor', max_length=100)
    estabelecimentos = models.ManyToManyField(Estabelecimento, through='Vinculo')

    def __str__(self):
        return self.user.username

class Vinculo(models.Model):
    estabelecimentos = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

class Estoque(models.Model):
    qtd = models.PositiveIntegerField('Quantidade')

    class Meta:
        ordering = ['qtd']

    def __str__(self):
        return self.qtd

class Vacina(models.Model):
    nome = models.CharField('Vacina', max_length=200, blank=False)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Coordenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    data_nascimento = models.DateField('Data de Nascimento')
    cpf = models.CharField('CPF',max_length=11)

    def __str__(self):
        return self.user.username
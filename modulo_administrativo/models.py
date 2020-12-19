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
    uf = models.ForeignKey(Uf)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Estabelecimento(models.Model):
    nome = models.CharField('UF', max_length=200, blank=False)
    cnes = models.CharField('CNES', max_length=45, blank=False)
    cnpj = models.CharField('CNPJ', max_length=14, blank=False)
    uf = models.ForeignKey(Uf)
    municipio = models.ForeignKey(Municipio)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return "%s - %s - %s" % (self.nome, self.cnes, self.cnpj)
from django.db import models
from moduloadministrativo.models import *
from modulocartaovacina.models import *

# Create your models here.
class Agenda(models.Model):
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    uf = models.ForeignKey(Uf,on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    data = models.DateTimeField('Data')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class Meta:
        ordering = ['data']

    def __str__(self):
        return self.data

ENUM_STATUS = [
    (1, 'Atendido'),
    (2, 'Espera'),
    (3, 'Não Compareceu'),
]

class FilaAtendimento(models.Model):
    status = models.SmallIntegerField(default=2, choices=ENUM_STATUS)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    observacao = models.CharField('Observação', max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['status']

    def __str__(self):
        return self.status
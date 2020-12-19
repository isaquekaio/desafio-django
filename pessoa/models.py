from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_coordenador = models.BooleanField(default=False)
    is_profissional = models.BooleanField(default=False)
    is_paciente = models.BooleanField(default=False)
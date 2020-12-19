from django.urls import path, include
from moduloadministrativo.views import *

urlpatterns = [
    path('', estabelecimento_listar, name='estabelecimento_listar'),
]
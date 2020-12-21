from django.urls import path
from modulocartaovacina.views import *

urlpatterns = [
    path('paciente', listar_paciente, name='listar_paciente'),
    path('paciente/cadastrar', cadastrar_paciente, name='cadastrar_paciente'),
    path('paciente/atualizar/<int:pk>', atualizar_paciente, name='atualizar_paciente'),

    path('cartao', listar_cartao_vacina, name='listar_cartao_vacina'),
    path('cartao/cadastrar', cadastrar_cartao_vacina, name='cadastrar_cartao_vacina'),
    path('cartao/atualizar/<int:pk>', atualizar_cartao_vacina, name='atualizar_cartao_vacina'),
]
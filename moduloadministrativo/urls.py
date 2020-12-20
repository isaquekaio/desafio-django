from django.urls import path
from moduloadministrativo.views import *

urlpatterns = [
    path('estabelecimento', listar_estabelecimento, name='listar_estabelecimento'),
    path('estabelecimento/cadastrar', cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
    path('estabelecimento/atualizar/<int:pk>', atualizar_estabelecimento, name='atualizar_estabelecimento'),
    #path('estabelecimento/excluir/<int:pk>', excluir_estabelecimento, name='excluir_estabelecimento'),

    path('vacina', listar_vacina, name='listar_vacina'),
    path('vacina/cadastrar', cadastrar_vacina, name='cadastrar_vacina'),
    path('vacina/atualizar/<int:pk>', atualizar_vacina, name='atualizar_vacina'),
    #path('vacina/excluir/<int:pk>', excluir_estabelecimento, name='excluir_estabelecimento'),
]
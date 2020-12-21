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

    path('fabricante', listar_fabricante, name='listar_fabricante'),
    path('fabricante/cadastrar', cadastrar_fabricante, name='cadastrar_fabricante'),
    path('fabricante/atualizar/<int:pk>', atualizar_fabricante, name='atualizar_fabricante'),
    path('fabricante/excluir/<int:pk>', excluir_fabricante, name='excluir_fabricante'),

    path('profissional', listar_profissional, name='listar_profissional'),
    path('profissional/cadastrar', cadastrar_profissional, name='cadastrar_profissional'),
    path('profissional/atualizar/<int:pk>', atualizar_profissional, name='atualizar_profissional'),

    path('coordenador', listar_coordenador, name='listar_coordenador'),
    path('coordenador/cadastrar', cadastrar_coordenador, name='cadastrar_coordenador'),
    path('coordenador/atualizar/<int:pk>', atualizar_coordenador, name='atualizar_coordenador'),

    path('estoque', listar_estoque, name='listar_estoque'),
    path('estoque/cadastrar', cadastrar_estoque, name='cadastrar_estoque'),

    path('estoque_item', listar_estoque_item, name='listar_estoque_item'),
    path('estoque_item/cadastrar', cadastrar_estoque_item, name='cadastrar_estoque_item'),

]
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

    path('vacina', listar_vacina, name='listar_vacina'),
    path('vacina/cadastrar', cadastrar_vacina, name='cadastrar_vacina'),
    path('vacina/atualizar/<int:pk>', atualizar_vacina, name='atualizar_vacina'),

    path('profissional', listar_profissional, name='listar_profissional'),
    path('profissional/cadastrar', cadastrar_profissional, name='cadastrar_profissional'),
    path('profissional/atualizar/<int:pk>', atualizar_profissional, name='atualizar_profissional'),


]
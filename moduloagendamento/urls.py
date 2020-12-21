from django.urls import path
from moduloagendamento.views import *

urlpatterns = [
    path('agenda', listar_agenda, name='listar_agenda'),
    path('agenda/cadastrar', cadastrar_agenda, name='cadastrar_agenda'),
    path('agenda/atualizar/<int:pk>', atualizar_agenda, name='atualizar_agenda'),

    path('fila', listar_fila, name='listar_fila'),
    path('fila/cadastrar', cadastrar_fila, name='cadastrar_fila'),
    path('fila/atualizar/<int:pk>', atualizar_agenda, name='atualizar_agenda'),

]
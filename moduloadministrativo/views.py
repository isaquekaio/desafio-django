from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Estabelecimento

# Create your views here.
def listar_estabelecimento(request):
    context = {
        'data': Estabelecimento.objects.order_by('-nome')[:10],
        'header': ['Nome', 'CNES', 'CNPJ', 'UF', 'Municipio', 'Ações'],
        'attributes': ['nome', 'cnes', 'cnpj', 'uf', 'municipio'],
        'link_create': 'cadastrar_estabelecimento',
        'link_update': 'atualizar_estabelecimento',
        'link_delete': 'excluir_estabelecimento',
        'title_page': 'Estabelecimentos',
        'title_aba': 'Estabelecimentos',
    }
    return render(request, 'pagina_generica/index.html', context)
    #return HttpResponse("Teste Listagem")

def cadastrar_estabelecimento(request):
    return HttpResponse("Teste Cadastrar")

def atualizar_estabelecimento(request, pk):
    return HttpResponse("Teste Atualizar")

def excluir_estabelecimento(request, pk):
    return HttpResponse("Teste Excluir")

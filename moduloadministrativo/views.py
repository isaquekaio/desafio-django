from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from moduloadministrativo.models import Estabelecimento
from moduloadministrativo.forms import *
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
    form = EstabelecimentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_estabelecimento')
    context = {
        'form': form,
        'title_page': 'Cadastrar Estabelecimento',
        'title_aba': 'Cadastrar Estabelecimento',
        'link_cancel': 'listar_estabelecimento',
    }
    return render(request, 'pagina_generica/form.html', context)
    #return HttpResponse("Teste Cadastrar")

def atualizar_estabelecimento(request, pk):
    model = get_object_or_404(Estabelecimento, pk=pk)
    form = EstabelecimentoForm(request.POST or None, instance=model)  # form preenchido

    if form.is_valid():
        form.save()
        return redirect('listar_estabelecimento')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Atualizar Estabelecimento',
        'title_aba': 'Atualizar Estabelecimento',
        'link_cancel': 'listar_estabelecimento',
    }
    return render(request, 'pagina_generica/form.html', context)
    #return HttpResponse("Teste Atualizar")

def excluir_estabelecimento(request, pk):
    model = get_object_or_404(Estabelecimento, pk=pk)
    model.delete()
    return redirect('listar_estabelecimento')
    #return HttpResponse("Teste Excluir")

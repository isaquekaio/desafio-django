from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from moduloadministrativo.models import *
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
"""
def excluir_estabelecimento(request, pk):
    model = get_object_or_404(Estabelecimento, pk=pk)
    model.delete()
    return redirect('listar_estabelecimento')
    #return HttpResponse("Teste Excluir")
"""

# CRUD Fabricante
def listar_fabricante(request):
    context = {
        'data': Fabricante.objects.order_by('nome')[:10],
        'header': ['Nome'],
        'attributes': ['nome'],
        'link_create': 'cadastrar_fabricante',
        'link_update': 'atualizar_fabricante',
        'link_delete': 'excluir_fabricante',
        'title_page': 'Fabricante',
        'title_aba': 'Fabricante',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_fabricante(request):
    form = FabricanteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_fabricante')
    context = {
        'form': form,
        'title_page': 'Cadastrar Fabricante',
        'title_aba': 'Cadastrar Fabricante',
        'link_cancel': 'listar_fabricante',
    }
    return render(request, 'pagina_generica/form.html', context)

def atualizar_fabricante(request, pk):
    model = get_object_or_404(Fabricante, pk=pk)
    form = FabricanteForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_fabricante')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Atualizar Fabricante',
        'title_aba': 'Atualizar Fabricante',
        'link_cancel': 'listar_fabricante',
    }
    return render(request, 'pagina_generica/form.html', context)

def excluir_fabricante(request, pk):
    model = get_object_or_404(Fabricante, pk=pk)
    model.delete()
    return redirect('listar_fabricante')

# CRUD vacina
def listar_vacina(request):
    context = {
        'data': Vacina.objects.order_by('-nome')[:10],
        'header': ['Nome', 'Estoque', 'Ações'],
        'attributes': ['nome', 'estoque'],
        'link_create': 'cadastrar_vacina',
        'link_update': 'atualizar_vacina',
        'link_delete': '',
        'title_page': 'Vacinas',
        'title_aba': 'Vacinas',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_vacina(request):
    form = VacinaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_vacina')
    context = {
        'form': form,
        'title_page': 'Cadastrar Vacina',
        'title_aba': 'Cadastrar Vacina',
        'link_cancel': 'listar_vacina',
    }
    return render(request, 'pagina_generica/form.html', context)

def atualizar_vacina(request, pk):
    model = get_object_or_404(Vacina, pk=pk)
    form = VacinaForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_vacina')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Atualizar Vacina',
        'title_aba': 'Atualizar Vacina',
        'link_cancel': 'listar_vacina',
    }
    return render(request, 'pagina_generica/form.html', context)

# CRUD para Profissional
def listar_profissional(request):
    context = {
        'data': Profissional.objects.order_by('user__username')[:10],
        'header': ['Usuario','Data Nascimento','CNS','CPF','RG','Orgao Expeditor','Estabelecimentos','Ações'],
        'attributes': ['user','data_nascimento','cns','cpf','rg','orgao_expeditor','estabelecimentos'],
        'link_create': 'cadastrar_profissional',
        'link_update': 'atualizar_profissional',
        'link_delete': '',
        'title_page': 'Profissional',
        'title_aba': 'Profissional',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_profissional(request):
    form = ProfissionalForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_profissional')
    context = {
        'form': form,
        'title_page': 'Cadastrar Profissional',
        'title_aba': 'Cadastrar Profissional',
        'link_cancel': 'listar_profissional',
    }
    return render(request, 'pagina_generica/form.html', context)

def atualizar_profissional(request, pk):
    model = get_object_or_404(Profissional, pk=pk)
    form = ProfissionalForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_profissional')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Atualizar Profissional',
        'title_aba': 'Atualizar Profissional',
        'link_cancel': 'listar_profissional',
    }
    return render(request, 'pagina_generica/form.html', context)

# CRUD Estoque
def listar_estoque(request):
    context = {
        'data': Estoque.objects.order_by('lote')[:10],
        'header': ['lote', 'movimento'],
        'attributes': ['lote', 'movimento'],
        'link_create': 'cadastrar_estoque',
        'link_update': '',
        'link_delete': '',
        'title_page': 'Estoque',
        'title_aba': 'Estoque',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_estoque(request):
    form = EstoqueForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_estoque')
    context = {
        'form': form,
        'title_page': 'Cadastrar Estoque',
        'title_aba': 'Cadastrar Estoque',
        'link_cancel': 'listar_estoque',
    }
    return render(request, 'pagina_generica/form.html', context)

# CRUD EstoqueItem
def listar_estoque_item(request):
    context = {
        'data': EstoqueItem.objects.order_by('saldo')[:10],
        'header': ['Quantidade', 'Saldo', 'Estoque', 'Vacina', 'Ação'],
        'attributes': ['qtd', 'saldo', 'estoque', 'vacina'],
        'link_create': 'cadastrar_estoque_item',
        'link_update': '',
        'link_delete': '',
        'title_page': 'Item do Estoque',
        'title_aba': 'Item do Estoque',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_estoque_item(request):
    form = EstoqueItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_estoque_item')
    context = {
        'form': form,
        'title_page': 'Cadastrar Estoque Item',
        'title_aba': 'Cadastrar Estoque Item',
        'link_cancel': 'listar_estoque_item',
    }
    return render(request, 'pagina_generica/form.html', context)


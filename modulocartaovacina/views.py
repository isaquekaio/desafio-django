from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from modulocartaovacina.models import *
from modulocartaovacina.forms import *

# Create your views here.
def listar_paciente(request):
    context = {
        'data': Paciente.objects.order_by('user__username')[:10],
        'header': ['Usuario','Data Nascimento','CPF','Ações'],
        'attributes': ['user','data_nascimento','cpf'],
        'link_create': 'cadastrar_paciente',
        'link_update': 'atualizar_paciente',
        'link_delete': '',
        'title_page': 'Paciente',
        'title_aba': 'Paciente',
    }
    return render(request, 'pagina_generica/index.html', context)
    #return HttpResponse("Teste Listagem")

def cadastrar_paciente(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_paciente')
    context = {
        'form': form,
        'title_page': 'Cadastrar Paciente',
        'title_aba': 'Cadastrar paciente',
        'link_cancel': 'listar_paciente',
    }
    return render(request, 'pagina_generica/form.html', context)
    #return HttpResponse("Teste Cadastro Paciente")

def atualizar_paciente(request, pk):
    model = get_object_or_404(Paciente, pk=pk)
    form = PacienteForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_paciente')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Cadastrar Paciente',
        'title_aba': 'Cadastrar paciente',
        'link_cancel': 'listar_paciente',
    }
    return render(request, 'pagina_generica/form.html', context)
    #return HttpResponse("Teste Atualizar Paciente")

# CDUD Cartão de Vacina
def listar_cartao_vacina(request):
    context = {
        'data': CartaoVacina.objects.order_by('paciente')[:10],
        'header': ['Data','Vacina','Profissional','Estabeleciemento','Paciente','Ações'],
        'attributes': ['data','vacina','profissional','estabelecimento','paciente'],
        'link_create': 'cadastrar_cartao_vacina',
        'link_update': 'atualizar_cartao_vacina',
        'link_delete': '',
        'title_page': 'Carta de Vacina',
        'title_aba': 'Carta de Vacina',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_cartao_vacina(request):
    form = CartaoVacinaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_cartao_vacina')
    context = {
        'form': form,
        'title_page': 'Registrar Vacina no Cartão',
        'title_aba': 'Registrar Vacina no Cartão',
        'link_cancel': 'listar_cartao_vacina',
    }
    return render(request, 'pagina_generica/form.html', context)

def atualizar_cartao_vacina(request, pk):
    model = get_object_or_404(Paciente, pk=pk)
    form = CartaoVacinaForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_cartao_vacina')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Atualizar Vacina no Cartão',
        'title_aba': 'Atualizar Vacina no Cartão',
        'link_cancel': 'listar_cartao_vacina',
    }
    return render(request, 'pagina_generica/form.html', context)
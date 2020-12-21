from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from moduloagendamento.models import *
from moduloagendamento.forms import *

# Create your views here.
def listar_agenda(request):
    context = {
        'data': Agenda.objects.order_by('data')[:10],
        'header': ['Vacina','UF','Municipio','Estabelecimento','data','paciente','Ações'],
        'attributes': ['vacina','uf','municipio','estabeleciemento','data','paciente'],
        'link_create': 'cadastrar_agenda',
        'link_update': 'atualizar_agenda',
        'link_delete': '',
        'title_page': 'Agendar',
        'title_aba': 'Agendar',
    }
    return render(request, 'pagina_generica/index.html', context)
    #return HttpResponse("Teste Listagem agenda")

def cadastrar_agenda(request):
    form = AgendaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_agenda')
    context = {
        'form': form,
        'title_page': 'Cadastrar Agendamento',
        'title_aba': 'Cadastrar Agendamento',
        'link_cancel': 'listar_agenda',
    }
    return render(request, 'pagina_generica/form.html', context)
    #return HttpResponse("Teste Cadastrar")

def atualizar_agenda(request, pk):
    model = get_object_or_404(Agenda, pk=pk)
    form = AgendaForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_agenda')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Cadastrar Agendamento',
        'title_aba': 'Cadastrar Agendamento',
        'link_cancel': 'listar_agenda',
    }
    return render(request, 'pagina_generica/form.html', context)
    #return HttpResponse("Teste Atualizar Agenda")

# CRUD referente ao Model Fila
def listar_fila(request):
    context = {
        'data': FilaAtendimento.objects.order_by('status')[:10],
        'header': ['Status', 'Agenda', 'observacao', 'Ações'],
        'attributes': ['status','agenda','observacao'],
        'link_create': 'cadastrar_fila',
        'link_update': 'atualizar_fila',
        'link_delete': '',
        'title_page': 'Fila de Atendimento',
        'title_aba': 'Fila de Atendimento',
    }
    return render(request, 'pagina_generica/index.html', context)

def cadastrar_fila(request):
    form = FilaAtendimentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_fila')
    context = {
        'form': form,
        'title_page': 'Fila de Atendimento',
        'title_aba': 'Fila de Atendimento',
        'link_cancel': 'listar_fila',
    }
    return render(request, 'pagina_generica/form.html', context)

def atualizar_agenda(request, pk):
    model = get_object_or_404(FilaAtendimento, pk=pk)
    form = FilaAtendimentoForm(request.POST or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('listar_fila')

    context = {
        'record': model,
        'form': form,
        'title_page': 'Atualizar Fila de Atendimento',
        'title_aba': 'Atualizar de Atendimento',
        'link_cancel': 'listar_fila',
    }
    return render(request, 'pagina_generica/form.html', context)
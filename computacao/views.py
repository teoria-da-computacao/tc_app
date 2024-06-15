from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Automato, ValidaSequencia
from .forms import SequenciaForm, AutomatoForm


def index(request):
    return render(request, 'computacao/index.html')


def afd0(request):

    a = ValidaSequencia()
    resultado = None
    sequencia = None

    if request.method == 'POST':
        form = SequenciaForm(request.POST)
        if form.is_valid():
            sequencia = form.cleaned_data['sequencia']
            resultado = a.validar(sequencia)

    context = {
        'form': SequenciaForm(),
        'resultado': resultado,
        'sequencia': sequencia,
        'descricao': a.descricao
    }
    return render(request, 'computacao/afd0.html', context)


def automato(request, automato_id):

    sequencia = None
    resultado = None

    form = SequenciaForm(request.POST or None)
    if form.is_valid():
        sequencia = form.cleaned_data['sequencia']
        resultado = Automato.objects.get(id=automato_id).valida_sequencia(sequencia)

    context = {
        'automato': Automato.objects.get(id=automato_id),
        'sequencia': sequencia,
        'resultado': resultado,
        'form': form,
    }
    return render(request, 'computacao/automato.html', context)
    # """return render(request, 'computacao/test.html', {'automato_id':automato_id})"""

def automatos(request):

    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)


def novo_automato(request):

    form = AutomatoForm(request.POST or None)
    if form.is_valid():
        new_automata = form.save()
        new_automata.desenha_diagrama()
        new_automata.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    context = {'form': form}

    return render(request, 'computacao/novo_automato.html', context)


def edita_automato(request, automato_id):
    """if request.POST == 'POST':
        form = AutomatoForm(request.POST)
        form.save()"""

    instance = Automato.objects.get(id=automato_id)
    form = AutomatoForm(request.POST or None, instance=instance)
    if form.is_valid():
        a = form.save()
        a.desenha_diagrama()
        a.save()
        return HttpResponseRedirect(reverse('computacao:automatos'))

    """
    form = AutomatoForm(initial={
        'nome': automato_a_editar.nome,
        'descricao': automato_a_editar.descricao,
        'alfabeto': automato_a_editar.alfabeto,
        'estados': automato_a_editar.estados,
        'estadoInicial': automato_a_editar.estadoInicial,
        'estadosDeAceitacao': automato_a_editar.estadosDeAceitacao,
        'dicionarioTransicao': automato_a_editar.dicionarioTransicao,
    })"""
    context = {'form': form, 'automato_id':automato_id}
    return render(request, 'computacao/edita_automato.html', context)

def apaga_automato(request, automato_id):
    Automato.objects.filter(id=automato_id).delete()
    context = {'automatos': Automato.objects.all()}
    return render(request, 'computacao/automatos.html', context)

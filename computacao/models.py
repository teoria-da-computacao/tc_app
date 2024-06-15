# Create your models here.
from django.db import models
from graphviz import Digraph
import os
from django.conf import settings


class Automato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    alfabeto = models.CharField(max_length=100)
    estados = models.CharField(max_length=100)
    estadoInicial = models.CharField(max_length=100)
    estadosDeAceitacao = models.CharField(max_length=100)
    dicionarioTransicao = models.CharField(max_length=1000)
    diagrama = models.FileField(upload_to='afd_diagrams/', blank=True, null=True)

    def __str__(self):
        return self.descricao

    def printAlfabeto(self):
        return str(set(self.alfabeto.split()))

    def printEstados(self):
        return str(set(self.estados.split()))

    def printEstadosDeAceitacao(self):
        return str(set(self.estadosDeAceitacao.split()))

    def dTransInTable(self):
        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        table = []

        linha = ['']
        for simbolo in self.alfabeto.split():
            linha.append(simbolo)
        table.append(linha)

        for estado in self.estados.split():
            linha =[estado]
            for simbolo in self.alfabeto.split():
                linha.append(dTrans[(estado, simbolo)])
            table.append(linha)

        return table

    def valida_sequencia(self, sequencia):

        estado = self.estadoInicial

        dTrans = {(t.split('-')[0], t.split('-')[1]):t.split('-')[2] for t in self.dicionarioTransicao.split()}

        for simbolo in sequencia:
            if simbolo in self.alfabeto:
                estado = dTrans[(estado, simbolo)]
            else:
                return False

        if estado in self.estadosDeAceitacao:
            return True
        else:
            return False


    def desenha_diagrama(self):

        d = Digraph(name=self.descricao)

        # configurações gerais
        d.graph_attr['rankdir'] = 'LR'
        d.edge_attr.update(arrowhead='vee', arrowsize='1')
        # d.edge_attr['color'] = 'blue'
        d.node_attr['shape'] = 'circle'
        # d.node_attr['color'] = 'blue'

        # Estado inicial
        d.node('Start', label='', shape='none')

        # Estados de transição
        estadosDeTransicao = set(self.estados.split()) - set(self.estadosDeAceitacao.split())
        for estado in estadosDeTransicao:
            d.node(estado)

        # Estado aceitação
        for estado in self.estadosDeAceitacao.split():
            d.node(estado, shape='doublecircle')

        # Transicoes
        d.edge('Start', self.estadoInicial)

        for transicao_comma in self.dicionarioTransicao.split():
            transicao = transicao_comma.split('-')
            d.edge(transicao[0], transicao[2], label=transicao[1])

        d.format = 'svg'
        # self.diagrama = f"project/computacao/images/afd/{str(self.nome).replace(' ', '_')}.svg"
        # d.render(f"project/computacao/static/computacao/images/afd/{str(self.nome).replace(' ', '_')}")

        file_name = f"{str(self.nome).replace(' ', '_')}.svg"
        file_path = os.path.join(settings.MEDIA_ROOT, 'afd_diagrams', file_name)
        # d.render(file_path)
        svg_data = d.pipe(format='svg')

        # Write the SVG data to the file
        with open(file_path, 'wb') as f:
            f.write(svg_data)

        self.diagrama.name = f"afd_diagrams/{file_name}"
        self.save()

class ValidaSequencia():
    descricao = 'AFD que aceita sequências binárias terminadas em 0'
    alfabeto = '01'
    estados = ['A', 'B']
    estadoInicial = 'A'
    estadosDeAceitacao = {'B'}
    dicionarioTransicao = {
        ('A', '0'): 'B',
        ('A', '1'): 'A',
        ('B', '0'): 'B',
        ('B', '1'): 'A'
    }

    def validar(self, sequencia):
        # Autómato em funcionamento
        estado = self.estadoInicial

        for simbolo in sequencia:
            if simbolo in self.alfabeto:
                estado = self.dicionarioTransicao[(estado, simbolo)]
            else:
                break

        if estado in self.estadosDeAceitacao:
            return True
        else:
            return False

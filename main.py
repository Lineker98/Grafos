
import info
import busca
import CaminhoMinimo
import time
import CaixeiroViajante
import os

#Leitura do arquivo fonte do grafo
fileName = input("Arquivo do grafo: ")
file = open(fileName)

str = file.readline()
str = str.split(" ")
numVertices = int(str[0])
numArestas = int(str[1])

#Preenchimento das estruturas de dados
listaAdj = [[] for x in range(numVertices)]
matAdj = [[0 for x in range(numVertices)] for x in range(numVertices)]
vertices = [x for x in range(numVertices)]
arestas = []


for i in range(0, numArestas):
    str = file.readline()
    str = str.split(" ")
    origem = int(str[0])
    destino = int(str[1])
    peso = float(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))
#print(listaAdj)
#print(matAdj)
#print(arestas)
n = len(listaAdj)
s = []
l = []
opcao = 0


def MSG_Menu():
    print(20 * '-'+ 'Menu de Opçoes' + '-'* 20)
    print('Informe o tipo de Pesquisa que deseja realizar:\n' +
               '1 - Informações do Grafo :\n' +
               '2 - Buscas no grafo :\n' +
               '3 - Pesquisas de Caminhos mínimos: \n' +
               '4 - Caixeiro Viajante: \n' +
               '5 - Sair')


def Menu_Operacoes(op):
    print(20 * '-' + 'Informe a operação que deseja Realizar' + '-'* 20)
    if op == 1:
        print('Operaçõos: \n' +
                '1 - Densidade\n' +
                '2 - Complemento\n' +
                '3 - Completo\n' +
                '4 - Regular\n' +
                '5 - SAIR DO MÓDULO\n')
    elif op == 2:
        print('Operações: \n' +
                   '1 - Busca Largura\n' +
                   '2 - Profundidade\n' +
                   '3 - Busca prof Recursiva\n' +
                   '4 - Componentes Conexas\n' +
                   '5 - Ordem Topológica\n' +
                   '6 - SAIR DO MODULO\n')
    elif op == 3:
        print('Operações: \n' +
                    '1 - Djisktra:\n' +
                    '2 - Bellman Ford:\n' +
                    '3 - Floyd Warshall\n' +
                    '4 - SAIR DP MÓDULO\n')


def SubMenuInfo(opcao, vertices, arestas, matAdj):

    op = 0

    while op != 5:
        Menu_Operacoes(opcao)
        op = int(input('Digite sua opção: \n'))
        if op == 1:
            densidade = info.densidade(vertices, arestas)
            print("Densidade: %.2f" % densidade)
        elif op == 2:
            complemento = info.complemento(matAdj)
            print("Complemento:", complemento)
            print("Original:   ", matAdj)
        elif op == 3:
            if (info.completo(matAdj)):
                print("Grafo completo!")
            else:
                print("Grafo NAO completo")
        elif op == 4:
            regular = info.regular(matAdj)
            print(f'Regular = {regular}')
        elif op == 5:
            print('SAINDO DO MÓDULO...')
            time.sleep(1)
            break


def SubMenuBusca(opcao, listaAdj):

    op = 0

    while op != 6:
        Menu_Operacoes(opcao)
        op = int(input('Digite sua opção: \n'))
        if op == 1:
            busca.buscaLargura(listaAdj, 0)
        if op == 2:
            busca.Busca_Prof(listaAdj, 0)
        if op == 3:
            busca.buscaProfRec(listaAdj, 0)
        if op == 4:
            busca.Componentes_Conexas(listaAdj)
        if op == 5:
            busca.Ord_Topologica(listaAdj)


def SubMenuCaminho(opcao, listaAdj, matAdj, s, t):

    op = 0

    while op != 4:
        Menu_Operacoes(opcao)
        op = int(input('Digite sua opção: \n'))
        if op == 1:
            inicio = time.time()
            print(inicio)
            CaminhoMinimo.Dijkstra(listaAdj, s, t)
            fim = time.time()
            print(fim)
            print(f'Tempo de execução de Dijkstra = {fim - inicio}s')
            print('-' * 30)
        if op == 2:
            inicio = time.time()
            CaminhoMinimo.BellmanFord(listaAdj, arestas, s, t)
            fim = time.time()
            print(f'Tempo de execução de Bellman Ford = {fim - inicio}s')
            print('-' * 30)
        if op == 3:
            inicio = time.time()
            CaminhoMinimo.FloydWarshall(matAdj, s, t)
            fim = time.time()
            print(f'Tempo de execução de FloydWarshall = {fim - inicio}s')
            print('-' * 30)
        if op == 4:
            print('SAINDO DO MODULO...')
            time.sleep(1)
            break

#Interacao com o usuario
while opcao != 5:
    MSG_Menu()
    opcao = int(input('Digite sua Opcao: \n'))

    if opcao == 1:
        SubMenuInfo(opcao, vertices, arestas, matAdj)
    if opcao == 2:
        SubMenuBusca(opcao, listaAdj)
    if opcao == 3:
        print(f'Seu grafo possui vértices de 0 a {n-1}')
        s = int(input('Informe qual o vértice de partida: \n'))
        t = int(input('Informe o vértice de destino: \n'))
        SubMenuCaminho(opcao, listaAdj, matAdj, s, t)
    if opcao == 4:
        print(f'Grafo: {fileName}')
        s = CaixeiroViajante.NearestNeighbor(listaAdj)
        p = CaixeiroViajante.Avalia(s, matAdj)
        print(p)
        print('Processando refinamento...')
        l = CaixeiroViajante.TWOOPT(s, matAdj)
        p = CaixeiroViajante.Avalia(l, matAdj)
        print(f'Distância TwoPt: {p}')
        print(f'Rota: {l}')
    if opcao == 5:
        print('SAINDO DO PROGRAMA...')
        time.sleep(1)
        break
        





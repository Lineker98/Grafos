
import info
import busca
import CaminhoMinimo
import time
import CaixeiroViajante

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


#Interacao com o usuario
tp = int(input('Informe o tipo de Pesquisa que deseja realizar:\n' +
               '1 - Informações do Grafo :\n' +
               '2 - Buscas no grafo :\n' +
               '3 - Pesquisas de Caminhos mínimos: \n' +
               '4 - Caixeiro Viajante: '))
if tp == 1:
    op = int(input("Operacao: \n" +
                   "1 Densidade\n" +
                   "2 Complemento\n" +
                   "3 Completo\n" +
                   "4 Regular\n"))
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
elif tp == 2:
    op = int(input("Operacao: \n" +
                   "1 Busca Largura\n" +
                   "2 Profundidade\n" +
                   "3 Busca prof Recursiva\n" +
                   "4 Componentes Conexas\n" +
                   "5 Ordem Topológica\n"))

    if op == 1:
        busca.buscaLargura(listaAdj, 0)
    elif op == 2:
       busca.Busca_Prof(listaAdj, 0)
    elif op == 3:
        busca.buscaProfRec(listaAdj, 0)
    elif op == 4:
        busca.Componentes_Conexas(listaAdj)
    elif op == 5:
        busca.Ord_Topologica(listaAdj)
elif tp == 3:
    op = int(input('Informe qual função deseja usar para busca de caminho mínimo:\n' +
                    '1 - Djisktra:\n' +
                    '2 - Bellman Ford:\n' +
                    '3 - Floyd Warshall\n' +
                    '4 - Caixeiro Viajante\n'+
                    '5 - Refinamento - TWOOPT'))
    if op < 1 or op > 5:
        while op < 1 or op > 4:
            print('ENTRADA INVÁLIDA! dIGITE NOVAMENTE! ')
            op = int(input('Informe qual função deseja usar para busca de caminho mínimo:\n' +
                           '1 - Djisktra:\n' +
                           '2 - Bellman Ford:\n' +
                           '3 - Floyd Warshall\n' +
                           '4 - Caixeiro Viajante'))
    print(f'Seu grafo possui vértices somente de 0 a {n-1}')
    s = int(input(f'Informe o vértice que deseja inicar: \n'))
    if s < 0 or s > n-1:
        while s < 0 or s > n-1:
            print('ENTRADA INVÁLIDA! DIGITE NOVAMENTE! ')
            s = int(input(f'Informe o vértice que deseja inicar: \n'))
    t = int(input('Informe qual o vértice de destino final: \n'))
    if t < 1 or t > n:
        while t < 1 or t > n:
            print('ENTRADA INVÁLIDA! DIGITE NOVAMENTE! ')
            t = int(input('Informe qual o vértice de destino final: \n'))
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
elif tp == 4:
    print(f'Grafo: {fileName}')
    s = CaixeiroViajante.NearestNeighbor(listaAdj)
    p = CaixeiroViajante.Avalia(s, matAdj)
    print(p)
    print('Processando refinamento...')
    l = CaixeiroViajante.TWOOPT(s, matAdj)
    p = CaixeiroViajante.Avalia(l, matAdj)
    print(f'Distância TwoPt: {p}')
    print(f'Rota: {l}')




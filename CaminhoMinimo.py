def min(distancia, q):
    menor = float('inf')
    vertice = -1
    for i in q:
        if distancia[i] < menor:
            menor = distancia[i]
            vertice = i
    return vertice


def MostraDBF(pred, s, t):#trabalo com listas adjacentes: Dijkstra e Bellman-Ford
    aux = []
    b = t
    while b != s:
        a = pred[b]
        b = a
        aux.append(a)
    aux.reverse()
    for i in range(len(aux)):
        print(f'{aux[i]} ', end='-> ')
    print(f'{t}')



def MostraFW(pred, s, t):#Trabalhando com matriz de adjacentes: Floyd Warshall
    aux = []
    b = t
    while b != s:
        a = pred[s][b]
        b = a
        aux.append(a)
    aux.reverse()
    for i in range(len(aux)):
        print(f'{aux[i]} ', end='-> ')
    print(f'{t}')


def Dijkstra(listaAdj, s, t):
    if len(listaAdj[s]) == 0:
        print(f'NÃO EXISTE CAMINHO A PARTIR DE {s}')
        return False
    dist = [9999999 for v in range(len(listaAdj))]
    pred = [-1 for v in range(len(listaAdj))]
    dist[s] = 0
    q = [x for x in range(len(listaAdj))]
    while len(q) != 0:
        u = min(dist, q)
        q.remove(u)
        for v in listaAdj[u]:
            if dist[v[0]] > dist[u] + v[1]:
                dist[v[0]] = dist[u] + v[1]
                pred[v[0]] = u
    print('^^' * 30)
    print('-' * 10 + f'ORDEM PARA A CAMINHO MINIMO DE {s} A {t}' + '-' * 10)
    MostraDBF(pred, s, t)
    print(f'Peso de caminho mínimo do vértice {s} para o vértice {t} = {dist[t]}')



def BellmanFord(listaAdj, arestas, s, t):
    dist = [9999999 for v in range(len(listaAdj))]
    pred = [-1 for v in range(len(listaAdj))]
    dist[s] = 0
    for i in range(len(listaAdj)):
        for a in arestas:
            if dist[a[1]] > dist[a[0]] + a[2]:
                dist[a[1]] = dist[a[0]] + a[2]
                pred[a[1]] = a[0]
    for a in arestas:
        if dist[a[1]] > dist[a[0]] + a[2]:
            print('Existe ciclo de custo negativo!')
    print('Não existe ciclo de custo negativo!')
    print('-' * 10 + f'ORDEM PARA A CAMINHO MINIMO DE {s} A {t}' + '-' * 10)
    MostraDBF(pred, s, t)
    print(f'Peso de caminho mínimo do vértice {s} para o vértice {t} = {dist[t]}')


def FloydWarshall(matrisAdj, s, t):

    dist = [[999999 for i in range(len(matrisAdj))] for i in range(len(matrisAdj))]
    pred = [[-1 for i in matrisAdj] for i in matrisAdj]
    for i in range(len(matrisAdj)):
        for j in range(len(matrisAdj)):
            if i == j:
                dist[i][j] = 0
            elif matrisAdj[i][j] != 0:
                dist[i][j] = matrisAdj[i][j]
                pred[i][j] = i
    for k in range(len(matrisAdj)):
        for j in range(len(matrisAdj)):
            for i in range(len(matrisAdj)):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    print('-' * 10 + f'ORDEM PARA A CAMINHO MINIMO DE {s} A {t}' + '-' * 10)
    MostraFW(pred, s, t)
    print(f'Peso de caminho mínimo do vértice {s} para o vértice {t} = {dist[s][t]}')

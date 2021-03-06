from random import randint
import copy
import time


def NearestNeighbor(listAdj):
    vaux = -1
    naovisitados = [x for x in range(len(listAdj))]#Lista com todos os vértices
    visitado = [0 for x in range(len(listAdj))]#Lista de identificação para vértice já visitado
    u = 0
    s = []
    s.append(u)
    visitado[0] = 1 #Vértice de partida recebe visitado
    while len(naovisitados) != 1:
        menor = float('inf')
        for i in listAdj[u]:
            if i[1] < menor and visitado[i[0]] == 0:#Vertice destino não visitado e de menor peso
                menor = i[1]
                vaux = i[0]
        visitado[vaux] = 1
        s.append(vaux)
        naovisitados.remove(u)
        u = vaux
    s.append(s[0])
    return s

def TWOOPT(s, matAdj):
    a = []
    b = -1
    start = time.time()
    end = time.time()
    while end - start <= 60:
        end = time.time()
        I1 = randint(1, len(s)-2)
        I2 = randint(1, len(s)-2)
        if I1 != I2:
            a = copy.deepcopy(s)
            b = a[I1]
            a[I1] = a[I2]
            a[I2] = b
            if Avalia(a, matAdj) < Avalia(s, matAdj):
                s = copy.deepcopy(a)            
    return s


def Avalia(s, matAdj):
    custo = 0
    u = 0
    v = 0
    for i in range(len(s)-1):
        u = s[i]
        v = s[i+1]
        custo = custo + matAdj[u][v]
    return custo





        


from random import randint
import copy
import time


def NearestNeighbor(listAdj):
    peso = 0
    vaux = -1
    naovisitados = [x for x in range(len(listAdj))]#Lista com todos os vértices
    visitado = [0 for x in range(len(listAdj))]#Lista de identificação paa vértice já visitado
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
        peso += menor
        visitado[vaux] = 1
        s.append(vaux)
        naovisitados.remove(u)
        u = vaux
    s.append(s[0])
    peso += listAdj[s[len(s)-1]][s[0]][1]#Recebe ultimo peso do vértice de chegada [origem][destino][peso]
    print('-' * 30)
    print(f'Peso do ciclo de melhor caminho encontrado: {peso}')
    print('-' * 30) 
    print(f'Melhor ciclo Hamiltoniano encontrado: {s}')
    print('-' * 30)
    return s

def TWOOPT(s, listAdj):
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
            if Avalia(a, listAdj) < Avalia(s, listAdj):
                s = copy.deepcopy(a)            
    return s


def Avalia(s, listAdj):
    custo = 0
    u = -1
    v = -1
    for i in range(len(s)-1):
        u = s[i]
        v = s[i+1]
        custo = custo + listAdj[u][v-1][1]
    return custo





        


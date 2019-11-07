import copy


def densidade(vertices, arestas):
    d = len(arestas) / (len(vertices) * (len(vertices) - 1))
    return d


def complemento(matAdj):
    matComp = [[0 for x in range(len(matAdj))] for x in range(len(matAdj))]
    for i in range(len(matAdj)):
        for j in range(len(matAdj)):
            if i != j:
                if matAdj[i][j] == 0:
                    matComp[i][j] = 1

    return matComp


def completo(matAdj):
    for i in range(len(matAdj)):
        for j in range(len(matAdj[i])):
            if i != j:
                if matAdj[i][j] == 0:
                    return False
    return True


def regular(matrizAdj):
    prevDegree = None
    for i in range(0, len(matrizAdj)):
        degree = 0
        for j in range(0, len(matrizAdj[i])):
            if matrizAdj[i][j] != 0:
                degree = degree + 1
        if prevDegree != None and degree != prevDegree:
            return False
        prevDegree = degree
    return True




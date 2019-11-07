def buscaLargura(listaAdj, s):
    visitado = [0 for x in range(len(listaAdj))]
    visitado[s] = 1
    print(s)
    f = [s]
    while len(f) != 0:
        u = f.pop([0])
        for i in listaAdj[u]:
            if visitado[i] == 0:
                visitado[i] = 1
                print(i)
                f.append(i)


def Busca_Prof(listaAdj, s):
    visitado = [0 for i in range(len(listaAdj))]
    visitado[s] = 1
    print(s)
    p = [s]
    r = []
    while len(p) != 0:
        u = p[-1]
        existeAdj = False
        for v in listaAdj[u]:
            if visitado[v] == 0:
                visitado[v] = 1
                print(v)
                p.append(v)
                existeAdj = True
                break
            if not existeAdj:
                p.pop()


global visitado


def buscaProfRec(listaAdj, s):
    global visitado
    visitado = [0 for x in range(len(listaAdj))]
    prof(listaAdj, s)


def prof(listaAdj, u):
    global visitado
    visitado[u] = 1
    print(u)
    for i in listaAdj[u]:
        if visitado[i[0]] == 0:
            prof(listaAdj, i[0])


def Componentes_Conexas(listaAdj):
    global visitado
    visitado = [0 for i in range(len(listaAdj))]
    marca = 0
    for i in range(len(listaAdj)):
        if visitado[i] == 0:
            marca = marca + 1
            Prof_Con(listaAdj, i, marca)


def Prof_Con(listaAdj, u, marca):
    global visitado
    visitado[u] = marca
    print(u, marca)
    for v in listaAdj[u]:
        if visitado[v[0]] == 0:
            Prof_Con(listaAdj, v, marca)


global ordem


def Ord_Topologica(listaAdj):
    global visitado
    global ordem
    ordem = []
    visitado = [0 for i in range(len(listaAdj))]
    for v in listaAdj:
        if visitado[v] == 0:
            ProFord(listaAdj, v)
    print(ordem)


def ProFord(listaAdj, u):
    global oredem
    global visitado
    visitado[u] = 1
    for v in listaAdj[u]:
        if visitado[v[0]] == 0:
            ProFord(listaAdj, v[0])
    ordem.insert(0, u)
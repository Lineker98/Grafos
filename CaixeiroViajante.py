def NearestNeighbor(listAdj):
    peso = 0
    vaux = -1
    naovisitados = [x for x in range(len(listAdj))]
    visitado = [0 for x in range(len(listAdj))]
    u = 0
    s = []
    s.append(u)
    visitado[0] = 1
    while len(naovisitados) != 1:
        menor = float('inf')
        for i in listAdj[u]:
            if i[1] < menor and visitado[i[0]] == 0:
                menor = i[1]
                vaux = i[0]
        peso += menor
        visitado[vaux] = 1
        s.append(vaux)
        naovisitados.remove(u)
        u = vaux
    peso += listAdj[s[len(s)-1]][s[0]][1]
    s.append(s[0])
    print('-' * 30)
    print(f'Peso do ciclo de melhor caminho encontrado: {peso}')
    print('-' * 30) 
    print(f'Melhor ciclo Hamiltoniano encontrado: {s}')
    print('-' * 30)
    #return s
        


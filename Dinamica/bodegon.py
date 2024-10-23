"""
Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los
grupos que quieren sentarse a comer, y la cantidad de integrantes que conforma a cada uno.
Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de
personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar,
las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse.
Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que
ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad
de espacios vacíos). Indicar y justificar la complejidad del algoritmo.

Para esta resolución en RPL, devolver una lista con los valores de los grupos a ubicar,
en el orden original en el que se encontraban en el vector P.
"""

def reconstruirSolBodegon(OPT, P):
    i = len(OPT) - 1
    w = len(OPT[0]) - 1
    solucion = []
    while i > 0 and w > 0:
        if OPT[i][w] != OPT[i-1][w]:
            solucion.append(P[i-1])
            w -= P[i-1]
        i -= 1
    return solucion


def bodegon(W, P):
    n = len(P)
    OPT = [[0 for _ in range(W+1)] for _ in range(n+1)]
    # se agrega fila de ceros para OPT(0,W) = 0
    # se agrega fila de ceros para OPT(n,0) = 0

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            p = P[i-1]
            if p > w: # si no puedo ubicar a esa familia
                OPT[i][w] = OPT[i-1][w]
            else:
                OPT[i][w] = max(OPT[i-1][w], OPT[i-1][w-p] + p )
    return reconstruirSolBodegon(OPT, P)


def bodegon_mejor(W, P):
    n = len(P)
    dp = [0] * (W + 1)
    incluidos = [[] for _ in range(W + 1)]

    for i in range(n):
        for w in range(W, P[i] - 1, -1):
            if dp[w] < dp[w - P[i]] + P[i]:
                dp[w] = dp[w - P[i]] + P[i]
                incluidos[w] = incluidos[w - P[i]] + [i]

    return dp, incluidos



familias = [2, 4, 5, 3]
print(bodegon_mejor(11, familias))


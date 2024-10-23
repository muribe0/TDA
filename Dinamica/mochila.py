"""
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor,
y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos,
y devuelva qué elementos deben ser guardados para maximizar la ganancia total.
Indicar y justificar la complejidad del algoritmo implementado.
"""

def reconstruirSolMochila(OPT, elementos):
    solucion = []
    f = len(OPT) - 1
    c = len(OPT[0]) - 1
    while f > 0 and c > 0:
        if OPT[f][c] != OPT[f-1][c]:
            solucion.append(f-1)
            _, p = elementos[f-1]
            c -= p
        f -= 1
    return solucion

# Maximizar la ganancia consiste en agregar o no un elemento i.
# Si no se agrega, la mejor solucion es aquella que no lo tiene.
# Si se agrega, la mejor solucion es aquella que lo tiene, pero tiene W-Pi peso.

def mochila(elementos, W):
    n = len(elementos)

    OPT = [[0 for _ in range(W+1)] for _ in range(n+1)]
    # OPT(i,0) = 0
    # OPT(0,W) = 0

    for i in range(1, n+1): # para cada posible elemento i
        for w in range(1, W+1): # me fijo como se comportaria con una mochila de capacidad w
            v, p = elementos[i-1]
            if p > w: # si su peso es mayor a la capacidad, no lo puedo agregar
                OPT[i][w] = OPT[i-1][w]
            else:
                OPT[i][w] = max(OPT[i-1][w], v + OPT[i-1][w-p])

    return reconstruirSolMochila(OPT, elementos)

elementos = [(3, 2), (1, 2)]
print(mochila(elementos, 3)) # [3, 1]
print(mochila(elementos, 4)) # [3, 1])

elementos = [(3, 2), (1, 2), (2, 1), (3, 1)]
restulado = mochila(elementos, 3) # [3, 1]
print(restulado)
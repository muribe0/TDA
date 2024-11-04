# Primero implementare el Camino del Caballo como una reduccion a Camino Hamiltoniano

from grafo import *

def es_compatible(actual, visitados):
    return visitados.count(actual) == 1


def camino(grafo, vertices, actual, visitados):
    if len(visitados) == len(vertices):
        return es_compatible(actual, visitados)

    for w in grafo.adyacentes(actual):
        if w not in visitados:
            visitados.append(w)
            if es_compatible(actual, visitados) and camino(grafo, vertices, w, visitados):
                return True
            visitados.remove(w)
    return False

def camino_hamiltoniano(grafo):

    vertices = grafo.obtener_vertices()
    for v in vertices:
        visitados = [v]
        if camino(grafo, vertices, v, visitados):
            return visitados

    return []

def reducir(n):
    grafo = Grafo()
    movimientos = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    for i in range(1, n+1):
        for j in range(1, n+1):

            # Para cada casilla del tablero, se crean los vertices correspondientes
            grafo.agregar_vertice(f"{i}-{j}")

    for i in range(1, n+1):
        for j in range(1, n+1):

            # Para cada casilla t del tablero, se crean aristas a los casilleros a los que se puede mover el caballo desde t

            for f,c in movimientos:
                if 1 <= i+f <= n and 1 <= j+c <= n and not grafo.estan_unidos(f"{i}-{j}", f"{i+f}-{j+c}"): # Si el movimiento es legal

                    grafo.agregar_arista(f"{i}-{j}", f"{i+f}-{j+c}")
    return grafo

def knight_tour(n):
    grafo = reducir(n)
    return camino_hamiltoniano(grafo) != []

# Solucion 2:

def es_valido(matriz):
    for fila in matriz:
        for celda in fila:
            if celda == 0:
                return False
    return True

def es_un_movimiento_valido(matriz, f, c, n):
    return 0 <= f < n and 0 <= c < n and matriz[f][c] == 0

def camino_caballo(matriz, f, c, movimientos, pasos):
    n = len(matriz)
    if pasos == n*n:
        return True

    for i,j in movimientos:
        if es_un_movimiento_valido(matriz, f+i, c+j, n):
            matriz[f+i][c+j] += pasos + 1

            if camino_caballo(matriz, f+i, c+j, movimientos, pasos + 1):
                return True
            matriz[f+i][c+j] = 0

    return False


def knight_tour(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    movimientos = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    matriz[0][0] = 1
    return camino_caballo(matriz, 0, 0, movimientos, 1)

print(knight_tour(8)) # Debería imprimir True


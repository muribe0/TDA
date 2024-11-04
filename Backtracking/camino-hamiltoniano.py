"""
Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez.
Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.
"""
from fontTools.ttLib.scaleUpem import visit

import grafo
from Greedy.grafo import Grafo


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


grafo1 = Grafo({
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
})

grafo2  = Grafo({
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'E', 'F'],
    'E': ['B', 'C', 'D'],
    'F': ['B', 'C', 'D']
})

def camino_hamiltoniano(grafo):

    vertices = grafo.obtener_vertices()
    for v in vertices:
        visitados = [v]
        if camino(grafo, vertices, v, visitados):
            return visitados

    return []

print(camino_hamiltoniano(grafo2))
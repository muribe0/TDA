"""
Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a #V,
devuelva si es posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.
Métodos del grafo:

Grafo(dirigido = False, vertices_init= []) para crear (hacer 'from grafo import Grafo')
agregar_vertice(self, v)
borrar_vertice(self, v)
agregar_arista(self, v, w, peso = 1)
el resultado será v <--> w
borrar_arista(self, v, w)
estan_unidos(self, v, w)
peso_arista(self, v, w)
obtener_vertices(self)
Devuelve una lista con todos los vértices del grafo
vertice_aleatorio(self)
adyacentes(self, v)
str
"""
from grafo import Grafo

def esCompatible(grafo, puestos, actual):
    for w in grafo.adyacentes(actual):
        if w in puestos:
            return False
    return True

def colocarVertice(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n:
        return True

    if v_actual == len(grafo):
        return False

    puestos.add(vertices[v_actual])
    if esCompatible(grafo, puestos, vertices[v_actual]) and colocarVertice(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return colocarVertice(grafo, vertices, v_actual + 1, puestos, n)


grafo = Grafo({
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
})

grafo2 = Grafo({
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F', 'H'],
})

print(colocarVertice(grafo, grafo.vertices(), 0, set(), 3))  # True
print(colocarVertice(grafo, grafo.vertices(), 0, set(), 4))  # False

print(colocarVertice(grafo2, grafo2.vertices(), 0, set(), 4))  # True

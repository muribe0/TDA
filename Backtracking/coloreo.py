"""
Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible
pintar cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.
Métodos del grafo:

    Grafo(dirigido = False, vertices_init = []) para crear (hacer 'from grafo import Grafo')
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

"""
1. Si todos los paises estan coloreados, devuelvo True
2. Pruebo colrear con un color el siguiente pais
3. Verifico si la solucion parcial es valida.
4. Si no lo es, retrocedo y vuelvo a probar con otro color
5. Si lo es, llamo recursivamente y vuelvo a 1 -> Si no encontramos solucion, volvemos a 2 a probar con otro color
6. Si llego aca, no hay solucion
"""

from grafo import Grafo

def esCompatible(grafo, colores, actual):
    for w in grafo.adyacentes(actual):
        if w in colores and colores[w] == colores[actual]:
            return False
    return True


def coloreo_rec(grafo, k, vertices, v_actual, colores):
    # Si ya encontre solucion, la devuelvo y termino
    # Avanzo si puedo
    # Pruebo si la solucion parcial es valida
    # Si no lo es, retrocedo y vuelvo a 2.
    # Si lo es, llamo recursivamente y vuelvo a 1
    # Si llegue hasta aca, ya probe con tod0 y no encontre una solucion.

    if len(colores) == len(vertices):
        return True

    actual = vertices[v_actual]

    for i in range(1,k+1):
        colores[actual] = i
        if esCompatible(grafo, colores, actual) and coloreo_rec(grafo, k, vertices, v_actual + 1, colores):
            return True
    else:
        del colores[actual]
        return False


def coloreo(grafo, k):
    vertices = grafo.vertices()
    colores = {}
    return coloreo_rec(grafo, k, vertices, 0, colores)


grafo = Grafo({
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
})
assert( coloreo(grafo, 3) == True ) # {'A': 1, 'B': 2, 'C': 3, 'D': 1, 'E': 2, 'F': 3}
assert( coloreo(grafo, 2) == False )

grafo2 = Grafo({
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F', 'H'],
})

assert( coloreo(grafo2, 4) == True ) # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 1, 'F': 2, 'G': 3, 'H': 4}
assert( coloreo(grafo2, 3) == True )
assert( coloreo(grafo2, 2) == False )

paises = Grafo({
    'ARG': ['BRA', 'CHI', 'URU', 'PAR', 'BOL'],
    'BRA': ['ARG', 'URU', 'PAR', 'BOL', 'PER', 'COL', 'VEN', 'GUY', 'SUR', 'FRE'],
    'CHI': ['ARG', 'PER', 'BOL'],
    'URU': ['ARG', 'BRA'],
    'PAR': ['ARG', 'BRA', 'BOL'],
    'BOL': ['ARG', 'BRA', 'CHI', 'PAR', 'PER'],
    'PER': ['BRA', 'CHI', 'BOL', 'ECU', 'COL'],
    'COL': ['BRA', 'PER', 'ECU', 'VEN'],
    'ECU': ['PER', 'COL'],
    'VEN': ['BRA', 'COL', 'GUY'],
    'GUY': ['BRA', 'VEN', 'SUR'],
    'SUR': ['BRA', 'GUY', 'FRE'],
    'FRE': ['BRA', 'SUR'],
})

assert (coloreo(paises, 4) == True)
assert (coloreo(paises, 3) == False)
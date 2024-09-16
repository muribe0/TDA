"""
Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al
menos uno de sus extremos en dicho conjunto. Por ejemplo, el conjunto de todos los vértices del grafo siempre será
un Vertex Cover.

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo
Vertex Cover del mismo.
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
1. Si ya encontre solucion, la devuelvo y termino
2. Avanzo si puedo
3. Pruebo si la solucion parcial es valida
    - Si no lo es, retrocedo y vuelvo a 2.
    - Si lo es, llamo recursivamente y vuelvo a 1
4. Si llegue hasta aca, ya probe con todo y no encontre una solucion.
"""
from grafo import Grafo
# para los vertices de vertex cover, me fijo si con sus aristas cubro completamente el grafo por dfs
# quito un vertice del vertex cover si puedo
# si no puedo, lo vuelvo a agregar y pruebo con otro vertice recursivamente
# si no puedo con ninguno, devuelvo False

# Solucion real:

# 1. Si llego al ultimo vertice y tengo un vertex cover, devuelvo el vertex cover
# 2. Iterar sobre los vertices tomando una de dos deciciones:
#    - Incluir el vertice en el cover
#    - No incluir el vertice en el cover
# 3. Si incluyo el vertice, llamo recursivamente con el siguiente vertice
# 3. Si no incluyo el vertice, llamo recursivamente con el siguiente vertice
# 4. Si llego aca, no hay solucion por esta rama



# Formar los ejes del grafo
def formarEjes(grafo):
    ejes = []
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if (v, w) not in ejes and (w, v) not in ejes:
                ejes.append((v, w))
    return ejes

def verticesOrdenados(grafo):
    apariciones = []
    for v in grafo.obtener_vertices():
        apariciones.append((len(grafo.adyacentes(v)), v))
    apariciones.sort(key=lambda x: x[0], reverse=True)  # Ordenamos de mayor a menor
    return [v[1] for v in apariciones]  # Devolvemos solo los vértices

def es_vertex_cover(grafo, cover, ejes):
    for u, v in ejes:
        if u not in cover and v not in cover:
            return False
    return True

def minimoVertex(grafo, ejes, vertices, indice, cover_actual, max_size):
    if len(cover_actual) > max_size:
        return None
    if indice == len(vertices):
        if es_vertex_cover(grafo, cover_actual, ejes):
            return cover_actual
        return None

    v = vertices[indice]

    # con v
    cover_con = minimoVertex(grafo, ejes, vertices, indice + 1, cover_actual + [v], max_size)
    if cover_con:
        return cover_con

    # si el cover no debe incluir a v, lo pruebo sin v

    # sin v
    cover_sin = minimoVertex(grafo, ejes, vertices, indice + 1, cover_actual, max_size)
    if cover_sin:
        return cover_sin

    return None

def vertexCover(grafo):
    ejes = formarEjes(grafo)
    vertices = verticesOrdenados(grafo)

    for max_size in range(len(vertices) + 1):
        cover = minimoVertex(grafo, ejes, vertices, 0, [], max_size)
        if cover:
            return set(cover)

    return set(grafo.obtener_vertices())

grafo2  = Grafo({
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'E', 'F'],
    'D': ['A', 'E', 'F'],
    'E': ['B', 'C', 'D'],
    'F': ['B', 'C', 'D']
})

print(vertexCover(grafo2))


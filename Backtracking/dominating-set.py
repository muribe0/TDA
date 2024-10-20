import grafo

"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien

(i) pertenece a D o bien;
(ii) es adyacente a un vértice en D.
"""

def es_dominating_set(vertices, solucion_parcial):
    for v in grafo.obtener_vertices():
        if v in solucion_parcial:
            continue
        tiene_adyacente = False


def dominating_set(grafo, vertices, indice, solucion_parcial, solucion_optima):
    if es_dominating_set(vertices, solucion_parcial): # poda (si ya encontre la solucion, es la mejor que encontrare por esta rama)
        return solucion_optima
    # if len(solucion_parcial) >= len(solucion_optima): # poda
        # return set(solucion_parcial)
    if indice == len(vertices):
        return solucion_optima

    v = vertices[indice]
    solucion_parcial.add(v)
    solucion_optima = dominating_set(grafo, vertices, indice + 1, solucion_parcial, solucion_optima)

    solucion_parcial.remove(v)
    solucion_optima = dominating_set(grafo, vertices, indice + 1, solucion_parcial, solucion_optima)

    return solucion_optima


def dominating_set_min(grafo):
    vertices = sorted(grafo.obtener_vertices(), key=lambda x: grafo.obtener_grado(x), reverse=True)
    solucion_parcial = set([])
    solucion_optima = set(vertices)

    return dominating_set(grafo, vertices, 0, solucion_parcial, solucion_optima)

grafo = grafo.Grafo({
    'A': ['B','C'],
    'B': ['A'],
    'C': ['A']
})

print(dominating_set_min(grafo))

# Optimizaciones a agregar:
# Si agregar un vertice no me amplia la solucion, no lo agrego
# Podrias empezar por los vertides de mayor grado
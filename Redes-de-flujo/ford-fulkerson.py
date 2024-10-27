from grafo import Graph, Vertex, Edge, ResidualGraph
from collections import deque

def bfs(grafo, inicio):
    cola = deque([inicio])

    while cola:
        actual = cola.popleft()
        if actual.visitado():
            continue
        actual.visitar()
        for eje in actual.obtener_edges():
            v = eje.obtener_hasta()
            if not v.visitado():
                cola.append(v)


def max_flow(graph, s, t):
    graph.set_all_flows(0)
    Gf = graph
    path = Gf.augmenting_path(s, t)
    while path: # No esta testeado pero se ve bastante OK. Sirve para entender bien como funciona el algoritmo
        Gf.augment(path)
        Gf = ResidualGraph(Gf)
        path = Gf.augmenting_path(s, t)
    return 0

def generar_grafo_simple():
    s = Vertex('s')
    A = Vertex('A')
    B = Vertex('B')
    C = Vertex('C')
    D = Vertex('D')
    t = Vertex('t')

    edges = [Edge(s, A, 3),
            Edge(s, B, 2),
            Edge(A, D, 2),
            Edge(B, A, 3),
            Edge(B, C, 3),
            Edge(C, t, 2),
            Edge(D, t, 3),
            Edge(D, B, 1)]

    grafo = Graph({s, A, B, C, D, t}, edges)

    s.add_edge(edges[0])
    s.add_edge(edges[1])
    A.add_edge(edges[2])
    B.add_edge(edges[3])
    B.add_edge(edges[4])
    C.add_edge(edges[5])
    D.add_edge(edges[6])
    D.add_edge(edges[7])

    return grafo, s, t

grafo1, s1, t1 = generar_grafo_simple()

resultado = max_flow(grafo1, s1, t1)
print(resultado)
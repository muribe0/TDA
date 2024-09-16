class Grafo:
    def __init__(self, _vertices=None):
        if _vertices is None:
            _vertices = dict()
        self._vertices = _vertices

    def vertices(self):
        return list(self._vertices.keys())

    def obtener_vertices(self):
        return list(self._vertices.keys())

    def agregar_vertice(self, nuevo):
        self._vertices[nuevo] = []

    def agregar_arista(self, a, b):
        self._vertices[a] = b
        self._vertices[b] = a

    def adyacentes(self, v):
        return self._vertices[v]

    def borrar_vertice(self, v):
        self._vertices.remove(v)
        for w in self._vertices.keys():
            if v in self._vertices[w]:
                self._vertices[w].remove(v)

    def estan_unidos(self, v, w):
        return w in self._vertices[v] or v in self._vertices[w]

    def obtener_grado(self, v):
        return len(self._vertices[v])

    def __len__(self):
        return len(self._vertices)

    def __str__(self):
        return str(self._vertices)
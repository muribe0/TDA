class Grafo:
    def __init__(self, _vertices=None):
        if _vertices is None:
            _vertices = dict()
        self._vertices = _vertices

    def vertices(self):
        return list(self._vertices.keys())

    def obtener_vertices(self):
        return list(self._vertices.keys())


    def adyacentes(self, v):
        return self._vertices[v]

    def estan_unidos(self, v, w):
        return w in self._vertices[v] or v in self._vertices[w]

    def __len__(self):
        return len(self._vertices)

    def __str__(self):
        return str(self._vertices)
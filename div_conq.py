class Matriz:
    def __init__(self, n, x=0, y=0):
        self.dim = n
        self.x = x
        self.y = y

    def obtenerSilo(self):
        return self.x, self.y

    def obtenerDim(self):
        return self.dim

    def incluye(self, s):
        if s.obtenerDim() == 1 and self.dim >= 1:
            return self.x + self.dim >= s.x and self.y + self.dim >= s.y


def sonMinimos(A, R):
    return A.obtenerDim() == 1 and R.obtenerDim() == 2

def generarSilo(M, X):
    x1, y1 = M.obtenerCoordenadas()
    x2, y2 = X.obtenerCoordenadas()

    xCentro = x1 + X.obtenerDim() - 1
    yCentro = x1 + X.obtenerDim() - 1

    # El centro es la X
    # # # #
    # X # #
    # # # #
    # # # #
    if x1 == x2:
        if y1 == y2:
            return Matriz(1, xCentro, yCentro)
        elif y2 > y1:
            return Matriz(1, xCentro, yCentro + 1)
    elif x2 > x1:
        if y2 == y1:
            return Matriz(1, xCentro + 1, yCentro)
        elif y2 > y1:
            return Matriz(1, xCentro + 1, yCentro + 1)

def dibujar(M, X, S):
    if not X.incleye(S):
        nuevoSilo = generarSilo(M, X)


def _dibujar(M, S):
    dibujar(M, S)

def main(n, x, y):
    M = Matriz(n)
    S = Matriz(1, x, y)
    _dibujar(M, S)

class Matriz:
    def __init__(self, n, x=0, y=0):
        self.dim = n
        self.x = x
        self.y = y
        self.excluido = None

        if n >= 2:
            self.cuadrantes = [Matriz(n//2, x, y), Matriz(n//2, x + n//2, y),
                               Matriz(n//2, x, y + n//2), Matriz(n//2, x + n//2, y + n//2)]

    def obtenerCuadrantes(self):
        return self.cuadrantes

    def obtenerSilo(self):
        return self.x, self.y

    def obtenerDim(self):
        return self.dim

    def incluye(self, s):
        if s.obtenerDim() == 1 and self.dim >= 1:
            return self.x + self.dim >= s.x and self.y + self.dim >= s.y

    def excluir(self, aExcluir):
        self.excluido = aExcluir

    def __repr__(self):
        return f'{self.x} - {self.x + self.dim}, {self.y} - {self.y + self.dim})'
def esMinimo(M):
    return M.obtenerDim() == 2

def generarPiezaCentral(M, X):
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
            # 1er cuadrante
            return X[1], Matriz(1, xCentro, yCentro)
        elif y2 > y1:
            # 3do cuadrante
            return X[3], Matriz(1, xCentro, yCentro + 1)
    elif x2 > x1:
        if y2 == y1:
            # 2er cuadrante
            return X[2], Matriz(1, xCentro + 1, yCentro)
        elif y2 > y1:
            # 4to cuadrante
            return X[4], Matriz(1, xCentro + 1, yCentro + 1)

def encontrarA(campo, S):
    for cuadrante in campo.obtenerCuadrantes():
        if cuadrante.incluye(S):
            return cuadrante

def colorear(matriz, cuadrante, codigo):
    x, y = cuadrante.obtenerSilo()
    for i in range(y, y + cuadrante.obtenerDim()):
        for j in range(x, x + cuadrante.obtenerDim()):
            matriz[i][j] = codigo
    matriz[y][x] = 1

def dibujar(matriz, campoGrande, cuadranteActual, S, codigo):
    if not cuadranteActual.incluye(S):
        cuadranteA, S = generarPiezaCentral(campoGrande, cuadranteActual)
    else:
        cuadranteA = encontrarA(cuadranteActual, S)
    cuadranteActual.excluir(cuadranteA)

    if esMinimo(cuadranteActual):
        colorear(matriz, cuadranteActual, codigo)
    else:
        for cuadrante in cuadranteActual.obtenerCuadrantes():
            codigo += 1
            dibujar(matriz, campoGrande, cuadrante, S, codigo)

def _dibujar(matriz, M, S):
    dibujar(matriz, M, M, S, 1)

def main(n, x, y):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    M = Matriz(n)
    S = Matriz(1, x, y)
    _dibujar(matriz, M, S)
    print(matriz)

main(4, 1, 1)
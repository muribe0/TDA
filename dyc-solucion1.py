class Matriz:
    def __init__(self, n, y=0, x=0):
        self.dim = n
        self.y = y
        self.x = x
        self.excluido = None

        if n >= 2:
            self.cuadrantes = [Matriz(n//2, y, x),        Matriz(n//2, y, x + n//2),
                               Matriz(n//2, y + n//2, x), Matriz(n//2, y + n//2, x + n//2)]

    def obtenerCuadrantes(self):
        return self.cuadrantes

    def obtenerDim(self):
        return self.dim

    def incluye(self, s):
        if s.obtenerDim() == 1 and self.dim >= 1:
            return self.y <= s.y <= self.y + self.dim - 1 and self.x <= s.x <= self.x + self.dim - 1

    def excluir(self, aExcluir):
        self.excluido = aExcluir

    def tieneExcluido(self):
        return self.excluido is not None

    def obtenerCoordenadasExcluido(self):
        return self.excluido.obtenerCoordenadas()

    def obtenerCoordenadas(self):
        return self.y, self.x
    def __repr__(self):
        return f'[{self.y} - {self.y + self.dim - 1}, {self.x} - {self.x + self.dim - 1}]'
def esMinimo(M):
    return M.obtenerDim() == 2

def generaryExcluirPiezaCentral(M, X):
    if X.tieneExcluido():
        return
    y1, x1 = M.obtenerCoordenadas()
    y2, x2 = X.obtenerCoordenadas()

    direccion = 0
    if x1 == x2:
        if y1 == y2:
            # X esta en el 1er cuadrante de M
            # por lo que el centro esta en la parte inferior derecha
            direccion = 3
        elif y2 > y1:
            # X esta en el 3er cuadrante de M
            # por lo que el centro esta en la parte superior derecha
            direccion = 1
    elif x2 > x1:
        if y2 == y1:
            # X esta en el 2do cuadrante de M
            # por lo que el centro esta en la parte inferior izquierda
            direccion = 2
        elif y2 > y1:
            # X esta en el 4to cuadrante de M
            # por lo que el centro esta en la parte superior izquierda
            direccion = 0

    cuadranteAnt = X
    cuadranteAct = X.obtenerCuadrantes()[direccion]
    while cuadranteAct.obtenerDim() > 1:
        cuadranteAnt.excluir(cuadranteAct)
        cuadranteAnt = cuadranteAct
        cuadranteAct = cuadranteAct.obtenerCuadrantes()[direccion]
    cuadranteAnt.excluir(cuadranteAct)

def encontrarA(campo, S):
    for cuadrante in campo.obtenerCuadrantes():
        if cuadrante.incluye(S):
            return cuadrante

def colorear(matriz, cuadrante, codigo):
    y, x = cuadrante.obtenerCoordenadas()
    for i in range(y, y + cuadrante.obtenerDim()):
        for j in range(x, x + cuadrante.obtenerDim()):
            matriz[i][j] = codigo
    excluidoY, excluidoX = cuadrante.obtenerCoordenadasExcluido()
    matriz[excluidoY][excluidoX] = 1

def dibujar(matriz, campoGrande, cuadranteActual, S, codigo):
    if not cuadranteActual.incluye(S):
        generaryExcluirPiezaCentral(campoGrande, cuadranteActual)
    else:
        cuadranteA = encontrarA(cuadranteActual, S)
        cuadranteActual.excluir(cuadranteA)

    if esMinimo(cuadranteActual):
        codigo[0] += 1
        colorear(matriz, cuadranteActual, codigo[0])
    else:
        for cuadrante in cuadranteActual.obtenerCuadrantes():
            dibujar(matriz, cuadranteActual, cuadrante, S, codigo)

def _dibujar(matriz, M, S):
    dibujar(matriz, M, M, S, [1])

def main(n, x, y):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    M = Matriz(n)
    S = Matriz(1, x, y)
    _dibujar(matriz, M, S)
    print(matriz)

    for f in matriz:
        print(f'{f},')

main(16, 3, 6)
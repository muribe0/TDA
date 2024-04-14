class Campo:
    def __init__(self, n, y=0, x=0):
        # Pre: n es potencia de 2 y mayor o igual a 2.
        #      y , x son enteros no negativos
        # Post: - Se crea un campo de dimension n x n, cuyas coordenadas de la esquina superior izquierda son (y, x)
        #       - Los cuadrantes se numeran de la siguiente manera:
        #         0 1
        #         2 3
        #       - El excluido es el cuadrante que contiene al silo o una pieza central especial
        #       - Para campos de dimension 2 o mas, se crean los cuadrantes hijos
        self.dim = n
        self.y = y
        self.x = x
        self.excluido = None

        if n >= 2:
            self.cuadrantes = [Campo(n // 2, y, x), Campo(n // 2, y, x + n // 2),
                               Campo(n // 2, y + n // 2, x), Campo(n // 2, y + n // 2, x + n // 2)]

    def obtenerCuadrantes(self):
        # Post: Devuelve los cuadrantes del campo
        return self.cuadrantes

    def obtenerDim(self):
        # Post: Devuelve la dimension de un lado del campo
        return self.dim

    def incluye(self, cuadrante):
        # Pre: cuadrante es un campo de dimension
        if 1 <= self.dim or cuadrante.obtenerDim() > self.dim:
            Exception('Dimensiones invalidas')
        return self.y <= cuadrante.y <= self.y + self.dim - 1 and self.x <= cuadrante.x <= self.x + self.dim - 1

    def excluir(self, aExcluir):
        if aExcluir.obtenerDim() >= self.dim:
            Exception('Dimensiones invalidas')
        if not self.tieneExcluido():
            self.excluido = aExcluir

    def tieneExcluido(self):
        return self.excluido is not None

    def obtenerExcluido(self):
        # Post: Devuelve el excluido, si no tiene excluido devuelve None
        return self.excluido

    def obtenerCoordenadasExcluido(self):
        # Post: Devuelve las coordenadas del excluido
        if not self.tieneExcluido():
            Exception('No tiene excluido')
        return self.excluido.obtenerCoordenadas()

    def obtenerCoordenadas(self):
        # Post: Devuelve las coordenadas superior izquierdas del campo
        return self.y, self.x

    def __repr__(self):
        return f'[{self.y} - {self.y + self.dim - 1}, {self.x} - {self.x + self.dim - 1}]'


def generaryExcluirPiezaCentral(cuadrantePadre, cuadranteActual):
    if cuadranteActual.tieneExcluido():
        return
    elif cuadrantePadre.obtenerExcluido().obtenerCoordenadas() == cuadranteActual.obtenerCoordenadas():
        direccion = 0
        cuadrante = cuadrantePadre.obtenerCuadrantes()[direccion]
        while cuadrante != cuadranteActual:
            direccion += 1
            cuadrante = cuadrantePadre.obtenerCuadrantes()[direccion]

    else:
        y2, x2 = cuadranteActual.obtenerCoordenadas()
        y1, x1 = cuadrantePadre.obtenerCoordenadas()

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

    cuadranteActual.excluir(cuadranteActual.obtenerCuadrantes()[direccion])


def encontrarSilo(campo, silo):
    for cuadrante in campo.obtenerCuadrantes():
        if cuadrante.incluye(silo):
            return cuadrante


def colorear(matriz, cuadrante, codigo):
    y, x = cuadrante.obtenerCoordenadas()
    for i in range(y, y + cuadrante.obtenerDim()):
        for j in range(x, x + cuadrante.obtenerDim()):
            matriz[i][j] = codigo[0]
    excluidoY, excluidoX = cuadrante.obtenerCoordenadasExcluido()
    codigo[0] += 1
    matriz[excluidoY][excluidoX] = codigo[0]


def dibujar(matriz, campoPadre, cuadranteActual, silo, codigo):
    if not cuadranteActual.incluye(silo):
        generaryExcluirPiezaCentral(campoPadre, cuadranteActual)  # O(1)
    else:
        cuadranteConSilo = encontrarSilo(cuadranteActual, silo)  # O(1)
        cuadranteActual.excluir(cuadranteConSilo)

    if cuadranteActual.obtenerDim() == 2:  # T(2) = O(1)
        codigo[0] += 1  # Esto permite identificarlos de forma distinta siempre
        colorear(matriz, cuadranteActual, codigo)
    else:
        for cuadrante in cuadranteActual.obtenerCuadrantes():  # T(n) = 4T(n/2)
            dibujar(matriz, cuadranteActual, cuadrante, silo, codigo)


def _dibujar(matriz, campo, silo):
    dibujar(matriz, campo, campo, silo, [1])


def main(n, x, y):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    campoEntero = Campo(n)
    silo = Campo(1, x, y)
    _dibujar(matriz, campoEntero, silo)


main(16, 3, 7)

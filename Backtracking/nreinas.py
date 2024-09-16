"""
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal
manera que ninguna pueda comerse con ninguna.

Nota: el ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se
describe.
"""

def sonCompatibles(columnas, filaActual, columnaActual):
    for f, c in columnas.items():
        if c == columnaActual and f == filaActual:
            continue
        if c == columnaActual or abs(f - filaActual) == abs(c - columnaActual):
            return False
    return True

def colocarReina(columnas, n, filaActual, columnaActual):
    if len(columnas) == n:
        return True

    for c in range(0, n):
        columnas[filaActual] = c
        if sonCompatibles(columnas, filaActual, c) and colocarReina(columnas, n, filaActual + 1, c):
            return True

    del columnas[filaActual]
    return False


def nreinas(n):
    filas = {}
    colocarReina(filas, n, filaActual=0, columnaActual=0)
    print(filas)
    return

print(nreinas(1)) # True

# Otra forma de hacerlo



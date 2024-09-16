"""
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada
posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). Por ejemplo, en el
arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

1. Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico: func
PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y
tiene como pre-condición que el arreglo tenga forma de pico.

2. Justificar el orden del algoritmo mediante el teorema maestro.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))". Por las
características de la herramienta, no podemos verificarlo de forma automática, pero se busca que se implemente con dicha
restricción
"""
from softwareproperties.gtk.utils import retry


# [1, 2, 3, 1, 0, -2]

def es_pico(v, m):
    if m == 0: # El pico puede estar en el 1er elemento
        return esta_decreciendo(v, m)
    elif m == len(v) - 1: # El pico puede estar en el ultimo elemento
        return esta_creciendo(v, m - 1)
    else:
        return v[m-1] < v[m] > v[m+1]

def esta_decreciendo(v, m):
    return m+1 < len(v) and v[m+1] < v[m]

def esta_creciendo(v, m):
    return m+1 < len(v) and v[m+1] > v[m]

def posicion_pico(v, ini, fin):
    mid = (ini + fin) // 2

    if ini > fin:
        return mid

    mid = (ini + fin) // 2
    if es_pico(v, mid):
        return mid
    # si me encuentro que el medio esta decreciendo, busco a la izq
    if esta_decreciendo(v, mid):
        return posicion_pico(v, ini, mid)

    # si me encuentro que el medio esta creciendo, busco a la der
    elif esta_creciendo(v, mid):
        return posicion_pico(v, mid, fin)

v = [1, 2, 3, 1, 0, -2, -4]
assert( posicion_pico(v, 0, len(v) - 1) == 2)

v = [1, 2, 3, 1, 0, -2]
assert( posicion_pico(v, 0, len(v) - 1) == 2)

v = [1, 3, 2]
assert( posicion_pico(v, 0, len(v) - 1) == 1)
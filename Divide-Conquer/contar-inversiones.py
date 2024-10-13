"""
Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos.
El arreglo A está completamente ordenado de menor a mayor. El arreglo B se encuentra desordenado.
Indicar, por división y conquista, la cantidad de inversiones necesarias al arreglo B para que quede
ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). Justificar el orden del
algoritmo mediante el teorema maestro.

en este ejercicio se pide cumplir la tarea "en tiempo mejor que O(n^2)".
"""
from heapq import merge
from mimetypes import inited

from TP2.tp2 import reconstruirSolucion


# 1 3 4 5 7 9
# 9 4 1 7 5 3

# 9 4 1  |  7 5 3

# 9 | 4 1   |  7 | 5 3

# 9 | 1 4   |  7 | 3 5    -> 1 + 1 = 2 inversiones

# 1 4 9  |   3 5 7    -> 2 + 2 = 4 inversiones

# 1 3 4 5 7 9  -> 2+1+1 = 4 inversiones
# total = 2 + 4 + 4 = 10 inv.

# 1 3 4 5
# 4 3 5 1
# 4 3   5 1 = 1+1=2 inversiones
# 3 4   1 5
# 1 3 4 5 = 2 inversiones. El 1, al ser insertado en la izq y la rama izq tener 2 elementos significa que son 2 inv.
# total = 2 + 2 = 4 inv

def merge(L, R, inv):
    resultado = []
    i = 0
    j = 0
    inversiones = inv
    while i < len(L) and j < len(R):
        dif = len(L) - i
        if L[i] <= R[j]:
            resultado.append(L[i])
            i+=1
        elif L[i] > R[j]:
            inversiones += dif
            resultado.append(R[j])
            j+=1
    resultado.extend(L[i:])
    resultado.extend(R[j:])

    return resultado, inversiones

def _contar_inversiones(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2

    L, invL = _contar_inversiones(arr[:mid])
    R, invR = _contar_inversiones(arr[mid:])

    return merge(L, R, invL+invR)


def contar_inversiones(A, B):

    return _contar_inversiones(B)[1]

print(contar_inversiones([1,3,4,5], [4,3,5,1]))

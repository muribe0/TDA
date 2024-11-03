C1, C2, C3, C4, C5, C6, C7, C8 = "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"
D1, D2, D3, D4, D5, D6, D7, D8 = "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"

def alternar_aux(arr, i, j):
    if j - i <= 2:
        return
    m = (i + j) // 2

    lenght = (j - i) // 4
    for k in range(i + lenght, m, 1):
        arr[k], arr[k + lenght] = arr[k + lenght], arr[k]

    alternar_aux(arr, i, m)
    alternar_aux(arr, m, j)

"""
Pasos:
0. Si el largo del arreglo es 2 o menos, no hacer nada.
1. Ordena la parte del centro del arreglo.
2. Divide en 2 partes el problema.
3. Vuelve al paso 0 para cada mitad

T(n) = 2T(n/2) + O(n/2) -> O(n log n)
"""

def alternar(arr):
    alternar_aux(arr, 0, len(arr))

arr = [C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8]
alternar(arr)
print(arr)
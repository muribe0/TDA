"""
Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). Se pide una función de orden
O(log(n)) que encuentre el índice del primer 0. Si no hay ningún 0 (solo hay unos), debe devolver -1.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "en O(log(n))". Por las características de la herramienta,
no podemos verificarlo de forma automática, pero se busca que se implemente con dicha restricción
"""
# 1 2 3 4 5 6 7 8 9 1 2 3 4

# 1 1 1 1 0 0 0 0 0 0 0 0 0
# 1 1 1 1 0
#       1 0
#         0
def encontrarCero(arr, l, r):
    if l > r:
        return -1

    m = (l + r) // 2
    if arr[l] == 0:
        return l
    elif arr[m] == 0:
        if m > 0 and arr[m-1] == 1:
            return m
        return encontrarCero(arr, l, m-1)
    elif arr[r] == 0:
        return  encontrarCero(arr, m+1, r)

    return -1

def indicePrimerCero(arr): return encontrarCero(arr, 0, len(arr)-1)

arr1 = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert( indicePrimerCero(arr1) == 4) # 4
assert( indicePrimerCero([]) == -1)
assert( indicePrimerCero([1]) == -1)
assert( indicePrimerCero([1, 1]) == -1)
assert( indicePrimerCero([1, 0]) == 1)
assert( indicePrimerCero([0, 0]) == 0)
assert( indicePrimerCero([1, 1, 0]) == 2)
assert( indicePrimerCero([1, 1, 1, 0]) == 3)
assert( indicePrimerCero([1, 1, 1, 0, 0, 0, 0]) == 3)
assert( indicePrimerCero([1, 1, 1, 1, 0, 0, 0, 0]) == 4)
assert( indicePrimerCero([1, 1, 1, 0, 0, 0, 0, 0]) == 3)
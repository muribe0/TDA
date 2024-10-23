"""
Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo
contiguo de máxima suma, utilizando División y Conquista. Indicar y justificar la complejidad del algoritmo.

Ejemplos:

[5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
[5, 3, -5, 4, -1] ->  [5, 3]
[5, -4, 2, 4, -1] -> [5, -4, 2, 4]
[5, -4, 2, 4] -> [5, -4, 2, 4]
[-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]
[3, 4, -1, 2, 1, -5] -> [3, 4, -1, 2, 1]
[3, 4, -1, 2, 1, -5, 6] -> [3, 4, -1, 2, 1, -5, 6]
[2, -3, 4, -1, 2, 1, -5, 4, 3, -2, 1, -4] -> [4, -1, 2, 1, -5, 4, 3]  8



[2][-3][4, -1, 2, 1]

       [4][-1][2, 1]

       [4][-1][2, 1]

              [2, 1]


Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista".
Por las características de la herramienta, no podemos verificarlo de forma automática,
pero se busca que se implemente con dicha restricción
"""

# Siempre hay 3 arreglos:
# Parte positiva, parte negativa, resto
#

def max_crossing_sum(arr, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1): # acumula la suma del 1ro hasta la mitad
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, high + 1): # acumula la suma desde la mitad al ultimo
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum

    return left_sum + right_sum

def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    return max(max_subarray_sum(arr, low, mid), # El max subarray esta en la izq
               max_subarray_sum(arr, mid + 1, high), # El max subarray esta en la der
               max_crossing_sum(arr, low, mid, high)) # El max subarray es combinar ambos

# Función principal para llamar al algoritmo
def find_max_subarray(arr):
    return max_subarray_sum(arr, 0, len(arr) - 1)

print(max_subarray_sum([3, 4, -1, 2, 1, -5, 6],0,6))
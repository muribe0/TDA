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
def find_negative_list(numbers, i):
    right_negative_limit = i
    sum_negative = numbers[i]
    for j in range(i, len(numbers)):
        current = numbers[j]
        if numbers[j] < 0:
            sum_negative += current
            right_negative_limit += 1
        else:
            return right_negative_limit, sum_negative
    return right_negative_limit, sum_negative


def merge(sum_left, sum_negative, sum_right):
    # Arreglar merge para contemplar casos en los que la der gane
    if sum_negative + sum_right < 0:
        return sum_left
    return sum_left + sum_negative + sum_right


def max_subset_iter(numbers, left=0):
    n = len(numbers)
    if left == n:
        return 0
    # 1 2 -3 2 2 -5 100
    sum_left = 0
    for i in range(left, len(numbers)):
        current = numbers[i]
        if current >= 0:
            sum_left += current
        else:
            right_negative_limit, sum_negative = find_negative_list(numbers, i)

            sum_rigth = max_subset_iter(numbers, right_negative_limit + 1)

            return merge(sum_left, sum_negative, sum_rigth)
    return sum_left
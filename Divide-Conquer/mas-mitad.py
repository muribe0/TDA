"""
Implementar una función (que utilice división y conquista) de orden O(n logn) que dado un arreglo
 de n números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces.
  Justificar el orden de la solución. Ejemplos:

[1, 2, 1, 2, 3] -> false
[1, 1, 2, 3] -> false
[1, 2, 3, 1, 1, 1] -> true
[1] -> true

Aclaración: Este ejercicio puede resolverse, casi trivialmente, ordenando el arreglo con un algoritmo eficiente,
 o incluso se puede realizar más rápido utilizando una tabla de hash. Para hacer interesante el ejercicio,
  resolver sin ordenar el arreglo, sino puramente división y conquista.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(n log(n))".
"""
# TODO NO ESTA TERMINADO

def _mas_mitad(arr, ini, fin):
    if fin - ini < 1:
        return arr[ini]
    medio = (ini + fin) // 2
    e1 = mas_mitad(arr, ini, medio)
    e2 = mas_mitad(arr, medio, fin)

    count1, count2 = 0, 0
    for i in range(ini, fin + 1):
        if e1 == arr[i]:
            count1 += 1
        if e2 == arr[i]:
            count2 += 1
    if count1 > medio + 1:
        return e1
    if count2 > medio + 1:
        return e2
    return None


def mas_mitad(arr):
    return _mas_mitad(arr, 0, len(arr)-1)
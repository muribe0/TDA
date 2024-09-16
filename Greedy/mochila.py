"""
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un
peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos, y devuelva qué
elementos deben ser guardados para maximizar la ganancia total. Indicar y justificar la complejidad del
algoritmo implementado. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.

¿Por qué se trata de un algoritmo Greedy? Justificar
"""
# cada elemento i de la forma (valor, peso)
# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elegidos = []
    # ordenar los elementos segun el ratio de valor/peso
    elementos.sort(key=lambda x: x[0]/x[1], reverse=True)

    for elemento in elementos:
        valor, peso = elemento
        if W >= peso:
            W -= peso
            elegidos.append(elemento)
        elif W == 0:
            return  elegidos

    return elegidos
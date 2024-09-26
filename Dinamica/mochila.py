"""
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor,
y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos de los elementos,
y devuelva qué elementos deben ser guardados para maximizar la ganancia total.
Indicar y justificar la complejidad del algoritmo implementado.
"""
def mejor(elementos, i, P, W):
    valor_i, peso_i = elementos[i]
    indice_mayor = i
    valor_mayor = valor_i
    peso_mayor = peso_i
    for j in range(0, i):
        valor_actual, peso_actual = elementos[j]
        if valor_actual >= valor_mayor:
            # ves si elegir el elemento j te aporta mas que elegir el i, y si hay espacio para bancarlo
            # agregar el elemento j es agregar el peso que acumula, mas el peso de agregarlo.
            # ademas, implica          agregar el valor que acumular, mas el valor de agregarlo.
            if P[j] + peso_actual <= W:
                valor_mayor = valor_actual
                indice_mayor = j

            peso_mayor = P[j] + peso_mayor
    return indice_mayor

def mochila(elementos, W):
    n = len(elementos)

    #g  3   |   1
    #p  2   |   2

    #   1.5 |  0.5
    M = [0] * n
    P = [0] * n

    M[0], P[0] = elementos[0][0], elementos[0][1]

    for i in range(1, n): # QUEREMOS CALCULAR, PARA CADA elemento: EL subset que maximiza
        j = mejor(elementos, i, P, W)
        valor, peso = elementos[j]
        M[i] = valor + M[j]
        P[i] = peso + P[j]

    return M

elementos = [(3, 2), (1, 2)]
print(mochila(elementos, 3)) # [3, 1]
print(mochila(elementos, 4)) # [3, 3]
print(mochila(elementos, 40)) # [3, 3]

elementos = [(3, 2), (1, 2), (1, 1)]
print(mochila(elementos, 3)) # [3, 4]
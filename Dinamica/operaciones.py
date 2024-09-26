"""
Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K,
 siendo que las operaciones posibles son:

(i) aumentar el valor del operando en 1;

(ii) duplicar el valor del operando.

Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones
a realizar (y cuáles son dichas operaciones). Desarrollar la ecuación de recurrencia.
Indicar y justificar la complejidad del algoritmo implementado. Aclaración: asegurarse de que el
algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'
"""


SUMAR = 'mas1'
DUPLICAR = 'por2'

def recornstruir_sol1(M):
    solucion = []
    i = len(M) - 1
    while i > 0:
        if M[i] == M[i-1] - 1:
            solucion.append(SUMAR)
        else:
            solucion.append(DUPLICAR)
        i -= 1

    return solucion


def operaciones(K):
    M = [0] * (K+1)
    M[0] = K
    # K, k-1 o K//2, k-2, K//4, k-3, K//8, k-4, ...
    for i in range(1, K):
        sumar = M[i-1] - 1
        duplicar = M[i-1] // 2 if M[i-1] % 2 == 0 else sumar
        M[i] = min(sumar, duplicar)
        if M[i] == 0:
            return recornstruir_sol1(M[:i+1])
    return recornstruir_sol1(M)

assert (operaciones(5) == [SUMAR, SUMAR, DUPLICAR, SUMAR]) # [5, 4, 2, 1, 0]
assert (operaciones(10) == [SUMAR, SUMAR, DUPLICAR, SUMAR, DUPLICAR]) # [10, 5, 4, 2, 1, 0]
# assert (operaciones(27) == [27, 26, 13, 12, 6, 3, 2, 1, 0])

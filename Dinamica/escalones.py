"""
Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar,
utilizando programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n.
Indicar y justificar la complejidad del algoritmo implementado.
Ejemplos:

n = 0 --> Debe devolver 1 (no moverse)
n = 1 --> Debe devolver 1 (paso de 1)
n = 2 --> Debe devolver 2 (dos pasos de 1, o un paso de 2)
n = 3 --> Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
n = 4 --> Debe devolver 7
n = 5 --> Debe devolver 13
"""
def escalera(n):
    M = [1, 1, 2] + [0] * (n-2)
    for i in range(3, n+1):
        M[i] = M[i-1] + M[i-2] + M[i-3]
    # opt(i) = opt(i-1) + opt(i-2) + opt(i-3)
    return M[n]

print(escalera(0))
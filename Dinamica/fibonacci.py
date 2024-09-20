"""
Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci.
Indicar y justificar la complejidad del algoritmo implementado.

Definición:

n = 0 --> Debe devolver 1
n = 1 --> Debe devolver 1
n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)
"""

def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    fib = [1, 1]

    for i in range(1, n):
        resultado = fib[0] + fib[1]
        fib[0] = fib[1]
        fib[1] = resultado
    return resultado

print(fibonacci(3))
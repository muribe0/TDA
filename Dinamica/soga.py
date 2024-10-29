"""
Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica,
permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes
resultantes sea máximo. El algoritmo debe devolver el valor del producto máximo alcanzable.
Tener en cuenta que la soga puede cortarse varias veces, como se muestra en el ejemplo con n = 10.
Indicar y justificar la complejidad del algoritmo.

Ejemplos:

n = 2 --> Debe devolver 1  (producto máximo es 1 * 1)
n = 3 --> Debe devolver 2  (producto máximo es 2 * 1)
n = 4 --> Debe devolver 4  (producto máximo es 2 * 2)
n = 5 --> Debe devolver 6  (producto máximo es 2 * 3)
n = 6 --> Debe devolver 9  (producto máximo es 3 * 3)
n = 7 --> Debe devolver 12  (producto máximo es 3 * 2 * 2)
n = 8 --> Debe devolver 18  (producto maximo es 3 * 3 * 2)
n = 9 --> Debe devolver 27  (producto maximo es 3 * 3 * 3)
n = 10 --> Debe devolver 36 (producto máximo es 3 * 3 * 2 * 2)
n = 11 --> Debe devolver 54 (producto máximo es 3 * 3 * 3 * 2)
"""

def corte_soga_optimo(n):
    if n < 2:
        return 0

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i): # recorro todos los cortes posibles de la soga de largo i
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
            # El mejor entre
            # a) no cortar
            # b) cortar en 2 partes
            # c) cortar en mas partes -> Esta infor esta en la lista

    return dp[n]

# Ejemplos de uso
for n in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
    print(f"n = {n} --> Producto máximo: {corte_soga_optimo(n)}")

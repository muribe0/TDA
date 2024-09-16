"""
Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada
de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5.
Justificar el orden del algoritmo.

Aclaración: no se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada,
ni de forma exacta ni aproximada.

Nota sobre RPL: en este ejercicio se pide cumplir la tarea "por división y conquista, en O(log(n))".
Por las características de la herramienta, no podemos verificarlo de forma automática, pero se busca
 que se implemente con dicha restricción
"""
# 64

# 32
# 0 31

# 15

def raizCuadrada(n, l, r):
    if l > r:
        return -1

    m = (l + r) // 2
    cuadrado = m ** 2
    cuadradoSig = (m+1) ** 2
    if cuadrado < n < cuadradoSig:
        return m
    if cuadrado > n:
        return raizCuadrada(n, l, m-1)
    elif cuadrado < n:
        return raizCuadrada(n, m+1, r)
    else:
        return m

def calcularRaiz(n): return raizCuadrada(n, 1, n)

print(calcularRaiz(1))
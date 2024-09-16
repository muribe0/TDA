"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes.
El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar,
y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada.

Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo.
¿Por qué se trata de un algoritmo Greedy? Justificar
"""

def encontrar_denominacion(monedas, monto):
    for m in monedas:
        if m <= monto:
            return m
    return 0

def cambio(monedas, monto):
    monedas.sort(reverse=True)
    vuelto = []
    restante = monto
    while restante > 0:
        m = encontrar_denominacion(monedas, restante)
        while m <= restante:
            vuelto.append(m)
            restante -= m

    return vuelto


print(cambio([1,2,5,10,20,50,100], 67))
"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que,
por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo
a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda.
Indicar y justificar la complejidad del algoritmo implementado.
"""


def reconstruirSolCambio(OPT, monedas):
    soluciones = []
    for j in range(len(monedas)):
        i = len(OPT) - 1 - j
        m = len(OPT[0]) - 1

        if OPT[i][m] != m:
            continue

        solucion_moneda_j = []
        while i > 0 and m > 0:
            d = monedas[i - 1]
            if m - d > 0:
                if OPT[i][m] == OPT[i][m-d] + d:
                    solucion_moneda_j.append(d)
                    m -= d
                elif OPT[i][m] == OPT[i-1][m-d] + d:
                    solucion_moneda_j.append(d)
                    m -= d
                    i -= 1
                else:
                    i -= 1
            elif OPT[i][m] == d:
                solucion_moneda_j.append(d)
                m -= d
                i -= 1
            else:
                i -= 1
        soluciones.append(solucion_moneda_j)

    if not soluciones:
        return []
    return min(soluciones, key=len)

def cambio(monedas, monto):
    monedas.sort()
    n = len(monedas)
    OPT = [[0 for _ in range(monto + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for m in range(1, monto + 1):
            d = monedas[i - 1]
            if d > m:
                OPT[i][m] = OPT[i - 1][m]
            else:
                caso1 = OPT[i - 1][m]
                caso2 = d
                caso3 = OPT[i - 1][m - d] + d if d + OPT[i - 1][m - d] <= m else 0
                caso4 = OPT[i][m - d] + d if OPT[i][m - d] + d <= m else 0
                OPT[i][m] = max(caso1, caso2, caso3, caso4)

    return reconstruirSolCambio(OPT, monedas)


C = [2, 5, 10]
resultado = cambio(C, 11)
[print(r) for r in resultado]

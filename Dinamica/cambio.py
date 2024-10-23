"""
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que,
por programación dinámica, reciba un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo
a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda.
Indicar y justificar la complejidad del algoritmo implementado.
"""


def reconstruirSolCambio(OPT, monedas):

    soluciones = []
    for j in range(len(monedas)): # para cada moneda, me puede fijar su solucion mejor e identificar cual tiene la menor cantidad de monedas involucradas
        i = len(OPT) - 1 - j
        m = len(OPT[0]) - 1

        if OPT[i][m] != m:
            continue # ignorar las soluciones que no lleguen al valor

        solucion_moneda_j = []

        while i > 0 and m > 0:
            d = monedas[i - 1]
            # si estan en orden: siempre voy a querer primero a la de mayor denom, asi que checkeo eso primero. Me fijo si se eligio a la misma moneda i.
            if m-d > 0 and OPT[i][m] == OPT[i][m-d] + d:
                solucion_moneda_j.append(d) # en ese caso, como se elegio a si mismo 2 veces o mas, debo seguir en la misma fila por si se elige de nuevo
                m -= d
                continue
            # el siguiente mejor caso es si elige usar la moneda i + el trabajo de la moneda anterior (i-1)
            elif m-d > 0 and OPT[i][m] == OPT[i-1][m-d] + d:
                solucion_moneda_j.append(d)
                m -= d
                i -= 1
                continue
            # el siguiente mejor es si se elige a si mismo, ya que significa que puede solanga
            elif OPT[i][m] == d:
                solucion_moneda_j.append(d)
                m -= d
                i -= 1
                continue
            # ultimo caso es que no le sirva la moneda i, por lo que se queda con el trabajo hecho por la moneda (i-1)
            # en este caso, no sabemos quien origina este resultado. Por lo que solo vamos a la fila donde podriamos encontrar la respuesta
            elif OPT[i][m] == OPT[i-1][m]:
                i -= 1
                continue
            else:
                i -= 1
        soluciones.append(solucion_moneda_j)
    mejor = 0
    for i in range(len(soluciones)):
        if len(soluciones[i]) < len(soluciones[mejor]):
            mejor = i
    if len(soluciones) == 0:
        return []
    return soluciones[mejor]


# Para un monto M y una moneda i con valor v tengo varias opciones
# Elijo la moneda para pagar y me quedo con lo anterior o no
# No la elijo -> me quedo con lo anterior

def cambio(monedas, monto):
    monedas.sort()  # esto me hace la vida mas facil
    n = len(monedas)
    OPT = [[0 for _ in range(monto + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for m in range(1, monto + 1):
            d = monedas[i - 1]
            if d > m:  # si no puedo elegir esa moneda sola
                OPT[i][m] = OPT[i - 1][m]
            elif d + OPT[i - 1][m - d] > m:  # si no puedo elegir la moneda actual + lo mejor de la anterior
                OPT[i][m] = max(OPT[i - 1][m], d, OPT[i][m - d] + d)
            elif OPT[i][m - d] + d > m:  # si no puedo elegir la moneda actual + la mejor ganancia de esa misma moneda
                OPT[i][m] = max(OPT[i - 1][m], OPT[i - 1][m - d] + d, d)
            else:
                OPT[i][m] = max(OPT[i - 1][m], OPT[i - 1][m - d] + d, d, OPT[i][m - d] + d)

    return reconstruirSolCambio(OPT, monedas)


C = [2, 5, 10]
resultado = cambio(C, 11)
[print(r) for r in resultado]

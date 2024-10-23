"""
Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco.
Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular.
Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa.
Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es la 1,
que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa se considera adyacente a las
casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas.
El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una casa,
los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos.
Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos.
El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible.
Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema.
Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar,
a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia correspondiente.
Indicar y justificar la complejidad del algoritmo propuesto.

Para esta resolución en RPL, devolver una lista con las posiciones de las casas a robar.
"""
# opt(i) = max( opt(i-1), opt(i-2) + gi )

def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0 if ganancias[0] >= ganancias[1] else 1]

    dp1 = [0] * (n-1)
    dp1[0] = ganancias[0]
    dp1[1] = max(ganancias[0], ganancias[1])
    for i in range(2, n-1):
        dp1[i] = max(ganancias[i] + dp1[i-2], dp1[i-1])

    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = ganancias[1]
    for i in range(2, n):
        dp2[i] = max(ganancias[i] + dp2[i-2], dp2[i-1])

    if dp1[-1] > dp2[-1]:
        casas_robadas = []
        i = len(dp1) - 1
        while i > 0:
            if dp1[i] == dp1[i-1]:
                i -= 1
            else:
                casas_robadas.append(i)
                i -= 2
        casas_robadas.append(0)
        return casas_robadas[::-1]
    else:
        casas_robadas = []
        i = len(dp2) - 1
        while i > 0:
            if dp2[i] == dp2[i-1]:

                i -= 1
            else:
                casas_robadas.append(i)
                i -= 2
        return casas_robadas[::-1]
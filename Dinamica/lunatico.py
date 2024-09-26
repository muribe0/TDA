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

def lunatuco(ganancias):
    n = len(ganancias)
    M = [0] * n
    M[0] = ganancias[0]
    M[-1] = ganancias[-1]
    for i in range(2, n):
        M[i] = max(M[i-1], M[i-2] + ganancias[i])
    return M

print(lunatuco([3, 2, 3, 1, 0, 5])) # [3, 0, 6, 6, 6, 11]
print(lunatuco([1, 2, 3, 1, 0, 5])) # [1, 0, 4, 4, 4, 9]
print(lunatuco([3, 2, 3, 1, 0, 5, 1])) # [3, 0, 6, 6, 6, 11, 7]
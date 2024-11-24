from typing import List

import pulp
from pulp import LpAffineExpression as Sumatoria


# LpAffineExpression es la forma en la que pulp maneja las sumatorias. No es necesario importarla, pero es útil para entender el código.


def mochila_variable(v: List[int], w: List[int], W: int):
    y = []
    problem = pulp.LpProblem("products", pulp.LpMaximize)
    for i in range(len(v)):
        y.append(pulp.LpVariable("y" + str(i), cat="Integer"))
        # Son los y_i de la ecuacion
        problem += y[i] <= 1
        problem += y[i] >= 0

    problem += Sumatoria([(y[i], w[i]) for i in range(len(y))]) <= W  # restriccion
    problem += Sumatoria([(y[i], v[i]) for i in range(len(y))])  # funcion a maximizar

    # agrega variables binarias (booleanas) y restricciones

    problem.solve()
    return list(map(lambda yi: pulp.value(yi), y))


if __name__ == "__main__":
    valores = [10, 1, 8, 100, 6, 11, 7, 2, 11]
    pesos = [6, 1, 3, 100, 4, 2, 8, 7, 9]
    W = 19
    y = mochila_variable(valores, pesos, W)
    print(y)
    print("Peso usado:", sum([pesos[i] * y[i] for i in range(len(y))]))
    print("Valor obtenido:", sum([valores[i] * y[i] for i in range(len(y))]))

# Output esperado:
# [0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
# Peso usado: 19
# Valor obtenido: 37

# Si elijo Integer y agregamos la restricción de que solo puede llevar un objeto de cada tipo, el output sería:
# [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -17.0, 1.0]
# Peso usado: 14.0
# Valor obtenido: 120.0

# Si elijo Integer y agregamos la restricción de que solo puede llevar un objeto de cada tipo, y no negativos el output
# sería:
# [-0.0, 1.0, 1.0, -0.0, 1.0, 1.0, -0.0, -0.0, 1.0]
# Peso usado: 19.0
# Valor obtenido: 37.0

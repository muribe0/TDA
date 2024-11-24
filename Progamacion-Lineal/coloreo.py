from typing import List
import pulp
from pulp import LpAffineExpression as Sumatoria

def coloreo(vertices, colores: int):
    paises = dict()
    problem = pulp.LpProblem("products", pulp.LpMinimize)
    problem += 0  # Dummy objective
    for id_v, adyacentes in vertices:
        pais = []
        for c in range(1, colores + 1):
            var = pulp.LpVariable(f"x_{id_v}_{c}", cat="LpBinary")
            pais.append(var)
        paises[id_v] = pais
        # \forall pais, \sum_c X_{pais,c} = 1
        problem += Sumatoria([(pais[i], 1) for i in range(len(pais))]) == 1

    # para cada valor de color posible,
    # para cada vertice v, la suma de los colores de los vertices adyacentes a v + v debe ser menor o igual a 1
    for c in range(1, colores + 1):
        for id_v, adyacentes in vertices:
            for id_ady in adyacentes:
                if id_ady in paises:  # Check if the adjacent vertex is in the dictionary
                    problem += paises[id_v][c-1] + paises[id_ady][c-1] <= 1  # restriccion

    # agrega variables binarias (booleanas) y restricciones

    problem.solve()
    return paises

# paises = [("A", ("B", "C")), ("B", ("D","E")), ("D", ("E",))]
paises = [(1, (2, 3)), (2, (4, 5)), (3, ()), (4, (5,)), (5, ())]
colores = 3
print(coloreo(paises, colores))

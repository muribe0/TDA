"""
Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen.
Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma
de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto
para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ].

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
Indicar y justificar la complejidad del algoritmo implementado."""


# [5, 4, 3, 2, 1]
# 5, 4+1, 3+2

# [8, 7, 6, 5, 5, 3, 1]
# 8, 7+1, 6, 5+3, 5

def bolsas(capacidad, productos):
    productos.sort(reverse=True)  # O(nlogn)
    izq = 0
    der = len(productos) - 1
    cantidad_bolsas = []

    while izq <= der:  # O(n)
        acum_izq = 0
        acum_der = 0
        bolsa_actual = []

        # llenar desde izq
        while izq <= der and acum_izq + productos[izq] <= capacidad:
            acum_izq += productos[izq]
            bolsa_actual.append(productos[izq])
            izq += 1

        # llenar desde der siq ueda espacio
        restante = capacidad - acum_izq
        while izq <= der and acum_der + productos[der] <= restante:
            acum_der += productos[der]
            bolsa_actual.append(productos[der])
            der -= 1

        cantidad_bolsas.append(bolsa_actual)

    return cantidad_bolsas

print(bolsas(9, [2,1,1,1,1,1,1,1]))
print(bolsas(9, [8, 5, 4, 3, 3, 2, 1, 1]))
print(bolsas(4, [4, 3, 3, 2, 2, 2, 1, 1]))

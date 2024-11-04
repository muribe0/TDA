def cubrir(ciudades):
    if len(ciudades) == 0:
        return []

    ciudades.sort(key=lambda x: x[1])
    nombres = []
    izq = ciudades[0][1]


    i = 1
    while i < len(ciudades):

        actual = ciudades[i][1]

        distancia = abs(actual - izq)

        if distancia > 50:
            izq = ciudades[i-1][1] + 51
            nombres.append(ciudades[i-1])
            while i < len(ciudades) and ciudades[i][1] < izq:
                i += 1
            if i < len(ciudades) and ciudades[i][1] >= izq:
                izq = ciudades[i][1]
                continue

        i += 1

    if izq <= ciudades[-1][1]:
        nombres.append(ciudades[-1])

    return nombres

# 156, 185, 206, 242, 270
# 206 -> izq: 207
#

list = [("Lezama", 156), ("Castelli", 185), ("Sevigne", 206), ("Gral Guido", 242), ("Maipú", 270), ("Dolores", 300), ("Chascomús", 349)]
# print(cubrir(list)) # Debería imprimir [Sevigne, Maipu]

def test_11_bifurcaciones_cobertura_con_1():
    list = [("Lezama", 156), ("Castelli", 160), ("Sevigne", 165), ("Gral Guido", 170), ("Maipú", 175), ("Dolores", 180), ("Chascomús", 185), ("Pila", 190), ("Ranchos", 195), ("Monte", 200), ("Las Flores", 205)]
    print(cubrir(list)) # Debería imprimir [Sevigne, Pila, Las Flores]

test_11_bifurcaciones_cobertura_con_1()
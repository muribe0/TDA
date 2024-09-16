# Para cada moneda,
# cuando le toca a sophi: agarrar la de mayor denominacion
# cuando le toca a marcos: agarrar la de menor denominacion

# Dado un arreglo de n monedas, y R el arreglo ordenado con cada moneda obtenida, donde los r_i son las monedas y
# las i pares o cero son de Sophi, las i impares son de Marcos.
# Se sabe que:
# i0 >= i1 -> i0-i1=ventaja >= 0
# i2 >= i3 -> ventaja ya es cero o mas + nueva ventaja >= 0
# ...
# ik >= ik+1 -> ventaja ya es cero o mas + nueva ventaja >= 0

# por lo que queda demostrado que Sophi siempre obtendra una ventaja positiva o nula frente a su hermano.
from random import randint


def ganaSophi(monedas):
    sophi = []
    mateo = []
    turno = 0
    while len(monedas) > 0:
        # empieza sophi

        if turno % 2 == 0:
            pos_mayor = -1 if monedas[-1] > monedas[0] else 0
            sophi.append(monedas.pop(pos_mayor))
        else:
            pos_menor = 0 if monedas[-1] > monedas[0] else -1
            mateo.append(monedas.pop(pos_menor))
        turno += 1
    return sophi, sum(sophi), mateo, sum(mateo)


listas = [[8, 3, 2, 9],
          [5, 5, 7, 4, 3, 8, 6, 2, 1, 1],
          [8, 2, 3, 9, 3, 4, 1, 3, 3, 2],
          [4, 5, 5, 10, 2, 1, 2, 10, 8, 10],
          [7, 10, 9, 1, 8, 6, 5, 1, 1, 1],
          [6, 1, 10, 4, 2, 6, 1, 2, 10, 10]]

print(ganaSophi(listas[0]))

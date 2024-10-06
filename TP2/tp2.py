# Maximizar la ganancia consiste en agregar o no un elemento i.
# Si no se agrega, la mejor solucion es aquella que no lo tiene.
# Si se agrega, la mejor solucion es aquella que lo tiene, pero tiene W-Pi peso.

# Maximizar la ganancia de Sophi consiste en agregar o no un elemento del fin/inicio

from math import ceil

def reconstruirSolucion(OPT):
    n = len(OPT)
    f = 0
    c = n - 1
    solucion = []
    turnoSophia = True
    while len(solucion) < ceil(n / 2):
        if not turnoSophia: # Si es el turno de Mateo
            if OPT[f][c] == monedas[c] - OPT[f][c-1]: # Si Mateo eligio el elemento del final
                c -= 1
            elif OPT[f][c] == monedas[f] - OPT[f+1][c]: # Si Mateo elegio el elemento del principio
                f += 1

        elif OPT[f][c] == monedas[c] - OPT[f][c-1]:  # Si Sophia eligio el elemento del final
            solucion.append(monedas[c])
            c -= 1
        elif OPT[f][c] == monedas[f] - OPT[f+1][c]:  # Si Sophia eligio el elemento del comienzo
            solucion.append(monedas[f])
            f += 1

        turnoSophia = not turnoSophia
    return solucion

def juego(monedas):
    n = len(monedas)
    OPT = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(j, -1, -1):
            largo = abs(i - j) + 1

            if largo == 1:
                # Caso base
                OPT[i][j] = monedas[i]
            elif largo == 2:
                # Caso base , dos monedas Sofia toma la mejor
                OPT[i][j] = abs(monedas[i] - monedas[j])
            else:
                # Si toma la primer moneda...
                if i == n - 1:
                    # Si toma la primer moneda, Mateo toma la mejor de las que quedan
                    OPT[i][j] = monedas[i] - OPT[i+1][j]
                # Si toma la ultima moneda...
                else:
                    # Si toma la ultima moneda, Mateo toma la mejor de las que quedan
                    OPT[i][j] = max(monedas[i] - OPT[i+1][j], monedas[j] - OPT[i][j-1])


    return reconstruirSolucion(OPT)


monedas = [5, 2, 1, 4, 7, 6]
resultado = juego(monedas)
print(resultado)
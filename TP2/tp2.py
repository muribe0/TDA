import difflib

def reconstruir_solucion(OPT, monedas):
    i, j = 0, len(monedas) - 1
    ganancia_sophi = 0
    ganancia_mateo = 0
    elecciones = []

    while i <= j:
        # Turno de Sophia
        if i == j:
            ganancia_sophi += monedas[i]
            elecciones.append(f"Sophia debe agarrar la primera ({monedas[i]})")
            break

        if monedas[i + 1] > monedas[j]:
            i_izq, j_izq = i + 2, j
        else:
            i_izq, j_izq = i + 1, j - 1
        tomar_izq = monedas[i] + OPT[i_izq][j_izq]

        if monedas[i] > monedas[j - 1]:
            i_der, j_der = i + 1, j - 1
        else:
            i_der, j_der = i, j - 2
        tomar_der = monedas[j] + OPT[i_der][j_der]

        if tomar_izq >= tomar_der:
            ganancia_sophi += monedas[i]
            elecciones.append(f"Sophia debe agarrar la primera ({monedas[i]})")
            i += 1
        else:
            ganancia_sophi += monedas[j]
            elecciones.append(f"Sophia debe agarrar la ultima ({monedas[j]})")
            j -= 1

        if monedas[i] > monedas[j]:
            ganancia_mateo += monedas[i]
            elecciones.append(f"Mateo agarra la primera ({monedas[i]})")
            i += 1
        else:
            ganancia_mateo += monedas[j]
            elecciones.append(f"Mateo agarra la ultima ({monedas[j]})")
            j -= 1

    resultado = "; ".join(elecciones)

    return resultado

def juego(monedas):
    n = len(monedas)
    OPT = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(j, -1, -1):
            largo = abs(i - j) + 1

            if largo == 1:
                OPT[i][j] = monedas[i]
            else:
                if monedas[i + 1] > monedas[j]:
                    i_izq = i + 2
                    j_izq = j
                else:
                    i_izq = i + 1
                    j_izq = j - 1

                if monedas[i] > monedas[j - 1]:
                    i_der = i + 1
                    j_der = j - 1
                else:
                    i_der = i
                    j_der = j - 2

                OPT[i][j] = max(monedas[i] + OPT[i_izq][j_izq], monedas[j] + OPT[i_der][j_der])

    return OPT

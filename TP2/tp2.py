from os import utime


def tp2(monedas):
    n = len(monedas)
    if n % 2 == 0:
        k = n // 2
    else:
        k = (n // 2) + 1

    OPT = [0 for _ in range(k)]

    izq = 0
    der = n - 1

    for i in range(k):
        primero = monedas[izq]
        ultimo = monedas[der]
        segundo = 0
        anteultimo = 0

        if izq + 1 < der:
            segundo = monedas[izq + 1]
            diferencia_por_primero = primero - max(segundo, ultimo)
        else:
            diferencia_por_primero = primero
        if der - 1 > izq:
            anteultimo = monedas[der - 1]
            diferencia_por_ultimo = ultimo - max(primero, anteultimo)
        else:
            diferencia_por_ultimo = ultimo

        if diferencia_por_primero >= diferencia_por_ultimo:
            OPT[i] = primero
            if segundo >= ultimo:
                der -= 2
            else:
                der -= 1
                izq += 1
        else:
            if primero >= anteultimo:
                der -= 1
                izq += 1
            else:
                der -= 2
            OPT[i] = ultimo

    return OPT

l1 = [5, 2, 1, 5, 7, 6, 4]
print(tp2(l1))

l2 = [3, 5, 10 ,7]
print(tp2(l2))
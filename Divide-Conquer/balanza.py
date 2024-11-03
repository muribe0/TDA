def balanza(joyas1, joyas2):
    if len(joyas1) != len(joyas2):
        raise ValueError("Las cantidades de joyas en ambos platos deben ser iguales")
    L, R = sum(joyas1), sum(joyas2)
    if L == R:
        return 0
    elif L > R:
        return 1
    else:
        return -1


def es_impar(x):
    return x % 2 == 1

def encontrar_aux(joyas, ini, fin):
    mid = (ini + fin) // 2
    cantidad = fin - ini

    if cantidad <= 1:
        return mid


    if es_impar(cantidad):
        res = balanza(joyas[ini:mid], joyas[mid+1:fin])

        if res == 0:
            return mid
        elif res == 1:
            return encontrar_aux(joyas, ini, mid)
        elif res == -1:
            return encontrar_aux(joyas, mid+1, fin)

    # else
    res = balanza(joyas[ini:mid], joyas[mid:fin])

    if res == 1:
        return encontrar_aux(joyas, ini, mid)
    elif res == -1:
        return encontrar_aux(joyas, mid, fin)



def encontrar_joya(joyas):
    # Ejemplo de uso de balanza: balanza(joyas[:2], joyas[2:4])
    return encontrar_aux(joyas, 0, len(joyas))

def test_encontrar_joya():
    L = [1, 5]
    print(encontrar_joya(L))
def test_3_joyas_primera():
    L = [5, 1, 1]
    print(encontrar_joya(L))
def test_3_joyas_tercera():
    L = [1, 1, 5]
    print(encontrar_joya(L))


test_3_joyas_tercera()
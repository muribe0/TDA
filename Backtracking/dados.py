def conv(tirada):
    return list(tirada)

def se_pasa(s, suma_actual):
    return suma_actual > s

def no_llegara(n, s, suma_actual):
    return suma_actual + n*6 < s

def se_pasara(n, s, suma_actual):
    return suma_actual + n > s

def dados(n, s, tiradas, tirada_actual, suma_actual):
    if n == 0 and suma_actual == s:
        tiradas.add(tuple(tirada_actual))
        return True

    if no_llegara(n, s, suma_actual):
        return False

    if se_pasara(n, s, suma_actual):
        return False

    if se_pasa(s, suma_actual):
        return False

    for d in range(6, 0, -1):

        tirada_actual.append(d)
        dados(n-1, s, tiradas, tirada_actual, suma_actual + d)
        tirada_actual.pop()

    return False

def sumatoria_dados(n, s):
    tiradas = set()
    d = 6
    while d > 0:
        tirada_actual = [d]
        suma_actual = d

        if se_pasa(s, suma_actual): # Poda
            d -= 1
            continue

        dados(n-1, s, tiradas, tirada_actual, suma_actual)


        d -= 1

    tiradas = list(tiradas)
    tiradas = list(map(conv, tiradas))
    return list(tiradas)



def test_sumatoria_dados():
    print(sumatoria_dados(3, 7))

test_sumatoria_dados()
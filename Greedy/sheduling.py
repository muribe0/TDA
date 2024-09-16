def se_solapan(fin_1, inicio_2):
    return fin_1 > inicio_2

def charlas(horarios):
    horarios = sorted(horarios, key=lambda x: x[1])
    charlas = []
    fin_ant = 0
    for h in horarios:
        inicio, fin = h
        if not se_solapan(fin_ant, inicio):
            charlas.append(h)
            fin_ant = fin

    return charlas

horarios = [(0, 1), (2, 5), (3, 4), (5, 6), (2, 4), (1, 3)]

print(charlas(horarios))
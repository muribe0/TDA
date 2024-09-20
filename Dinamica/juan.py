def calcularMejor(dias, j, mejor=[]):
    if 0 > j or j >= len(dias):
        return 0
    if j == 0:
        return dias[0]
    if j == 1:
        return dias[1]
    if mejor[j] != 0:
        return mejor[j]

    mejor[j] = max(dias[j] + calcularMejor(dias, j-2, mejor), calcularMejor(dias, j-1, mejor))
    return mejor[j]
best = [0]*6
dias = [10, 20, 15, 30, 20, 50]
print(calcularMejor(dias, len(dias)-1, best)) # 100
print(best)


def juan_el_vago(M, dias):
    G = [0] * dias
    G[0] = M[0]
    G[1] = max(M[1], M(0))

    for d in range(2, dias):
        G[d] = max(G[d-1], G[d-2] + M[d])

    return G[dias-1]

def construir_elecciones(G,M):
    elecciones = []
    d = len(G)-1
    while( d >= 0 ):
        opt_ayer = G[d-1] if d>0 else 0
        opt_anteayer = G[d-2] if d>1 else 0
        valor_hoy = M[d]
        if valor_hoy + opt_anteayer >= opt_ayer:
            elecciones.insert(0, d)
            d -= 2
        else:
            d -= 1

    return elecciones

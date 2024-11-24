def hay_otro_barco_adyacente(S, f, c, k):
    # funcion que verifica si hay un barco adyacente
    vecinas = [(f, c+1), (f+1, c-1), (f+1, c), (f+1, c+1)]
    for vf, vc in vecinas:
        if not (0 <= vf < len(S) and 0 <= vc < len(S[0])):
            continue
        if S[vf][vc] != -1 and S[vf][vc] != S[f][c]:
            return True
    return False

def verificador(S, filas, columnas, barcos):

    # Recorrer la matriz S
    n = len(S)
    m = len(S[0])
    k = len(barcos)

    if len(filas) != n or len(columnas) != m:
        return False

    for f in range(n):
        for c in range(m):
            if S[f][c] == -1:
                # si no hay barco en esa posicion, sigo con la siguiente casilla
                continue
            if S[f][c] >= k:
                # si el barco en esa posicion no es valido
                return False
            if filas[f] == 0 or columnas[c] == 0 or barcos[S[f][c]] == 0:
                # si no hay mas casilleros para ocupar en esa fila o columna
                return False
            if hay_otro_barco_adyacente(S, f, c, k):
                # si hay un barco adyacente
                return False
            barcos[S[f][c]] -= 1
            filas[f] -= 1
            columnas[c] -= 1

    return not any(filas) and not any(columnas) and not any(barcos)

def armar_S(filas, columnas, solucion):
    S = [[-1 for _ in range(len(columnas))] for _ in range(len(filas))]
    for i in range(len(solucion)):
        f, c = solucion[i]
        S[f][c] = i
    return S
"""
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin.
Además, cada charla tiene asociado un valor de ganancia. Implementar un algoritmo que,
utilizando programación dinámica, reciba un arreglo que en cada posición tenga una charla
representada por una tripla de inicio, fin y valor de cada charla, e indique cuáles son las
charlas a dar para maximizar la ganancia total obtenida. Indicar y justificar la complejidad del algoritmo implementado.
"""

"""
Estrategia:
1. Ordenar las charlas de forma ascendente segun el timepo de fin
2. Obtener la charla k para la cual el fin_k <= charla_i para cada i (para cada charla).
3. Obtener el mejor de cada charla segun opt(i) = max[ opt(i-1), opt(k) + charlas(i)  ]
"""

def calcularAnterior(charlas):
    # para cada charla, obtiene la charla anterior que podria haberse llevado a cabo
    resultado = [-1] * len(charlas)
    for i in range(len(charlas)-1, -1, -1):
        inicioAct = charlas[i][0]
        for j in range(i-1, -1, -1):
            finAnt = charlas[j][1]
            if finAnt <= inicioAct:
                resultado[i] = j
                break

    return resultado

def reconstruirSolucion(M, charlas, p):
    i = len(charlas) - 1
    solucion = []
    while i >= 0:
        if (p[i] >= 0 and  M[i] == M[p[i]] + charlas[i][2]) or i == 0:
            solucion.append(i)
            i = p[i]
        else:
            i -= 1
    return solucion

def scheduling(charlas):
    n = len(charlas)
    if n == 1:
        return charlas[0][2]

    charlas.sort(key=lambda x: x[1])

    p = calcularAnterior(charlas)

    M = [0] * n
    M[0] = charlas[0][2]
    for i in range(1, n): # opt(i) = max[ opt(i-1), opt(k) + charlas(i)  ] donde opt es M
        if p[i] >= 0:
            M[i] = max ( M[i-1], M[p[i]] + charlas[i][2])
        else:
            M[i] = max ( M[i-1], charlas[i][2])

    return reconstruirSolucion(M, charlas, p)

charlas = [(1, 3, 5),
           (2, 5, 6),
           (3, 7, 8),
           (4, 6, 7),
           (5, 8, 9),
           (6, 9, 10)]

def printCharlas(charlas):
    charlas.sort(key=lambda x: x[1])
    for i in range(len(charlas)):
        ini, fin, peso = charlas[i]
        linea = f"{i} -> {" "*ini}{"■"*fin}"
        faltante = 30 - len(linea)
        print(f"{linea}{" "*faltante} {peso}")

printCharlas(charlas)
print(scheduling(charlas))
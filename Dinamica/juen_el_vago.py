"""
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias,
pero no quiere trabajar dos días seguidos. Dado un arreglo con el monto esperado a ganar cada día,
determinar, por programación dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar
dos días seguidos. Hacer una reconstrucción para verificar qué días debe trabajar.
Indicar y justificar la complejidad del algoritmo implementado.
"""

def reconstruirSol1(M, trabajos):
    n = len(trabajos)
    i = n - 1
    solucion = []
    while i >= 0:
        if i >= 1 and M[i] == M[i-1]:
            i -= 1 # significa que uso el dia anterior, omitiendo el propio. Dejo que i avance

        else: # significa que uso el dia i-2 y el propio. Agrego el propio
            solucion.append(i)
            i -= 2
    return solucion[::-1]

def juan_el_vago(trabajos):
    n = len(trabajos)
    if n == 0:
        return []
    if n == 1:
        return [0]

    M = [0] * n
    M[0] = trabajos[0]
    M[1] = trabajos[1] if trabajos[1] >= trabajos[0] else trabajos[0]
    for i in range(2, n):
        M[i] = max( M[i-1], M[i-2] + trabajos[i] )
    return reconstruirSol1(M, trabajos)


assert(juan_el_vago([10, 25, 40, 30, 20, 50]) == [1, 3, 5]) # [1, 3, 5]
assert(juan_el_vago([10, 20, 15, 30, 20, 50]) == [1, 3, 5]) # [1, 3, 5]
assert(juan_el_vago([20, 10]) == [0]) # [0]
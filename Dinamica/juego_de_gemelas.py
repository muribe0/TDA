"""
Manejamos un negocio que atiende clientes en Londres y en California.
Nos interesa cada mes decidir si operar en una u otra ciudad.
Los costos de operación para cada mes pueden variar y son dados por 2 arreglos: L y C,
con valores para todos los meses hasta n. Naturalmente, si en un mes operamos en una ciudad,
y al siguiente en una distinta, habrá un costo fijo M por la mudanza. Dados los arreglos de
costos de operación en Londres (L) y California (C), indicar la secuencia de las n localizaciones
en las que operar durante los n meses, sabiendo que queremos minimizar el total de los costos de operación.
Se puede empezar en cualquier ciudad. Indicar y justificar la complejidad del algoritmo implementado.
"""

def reconstruirSolPlanMensual(OPT, OTRA, arreglo_OPT, arreglo_OTRA, nombre_OPT, nombre_OTRA):
    OPTIMOS = [OPT, OTRA]
    arreglos = [arreglo_OPT, arreglo_OTRA]
    nombres = [nombre_OPT, nombre_OTRA]
    z = 0

    n = len(OPT)
    i = n - 1
    solucion = []
    while i > 0:
        arreglo_actual = arreglos[z] # es el arreglo de la ciudad actual
        OPT_actual = OPTIMOS[z]      # es el arreglo de la ciudad que donde se comenzó y terminó  (mes 1 y n incluidos)

        solucion.append(nombres[z]) # siempre agrego la ciudad actual

        if OPT_actual[i] != OPT_actual[i - 1] + arreglo_actual[i]: # si se mudo
            z = 1 if z == 0 else 0 # doy vuelta z si es que cambio de ciudad

        i -= 1

    if i == 0:
        solucion.append(nombres[z])
    return solucion[::-1]

def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n = len(arreglo_L)

    L = [0] * n
    C = [0] * n

    L[0] = arreglo_L[0]
    C[0] = arreglo_C[0]

    # para Londres, si o si vas a usar el costo de laburar en ese mes. La pregunta es: venis de Cali o de londres?

    for i in range(1, n):
        L[i] = arreglo_L[i] + min(C[i - 1] + costo_M, L[i - 1])
        C[i] = arreglo_C[i] + min(L[i - 1] + costo_M, C[i - 1])
    print(L, C)
    if L[-1] > C[-1]:
        return reconstruirSolPlanMensual(C, L, arreglo_C, arreglo_L, "california", "londres")
    else:
        return reconstruirSolPlanMensual(L, C, arreglo_L, arreglo_C, "londres", "california")


arreglo_L = [4, 5, 2, 1, 7]
arreglo_C = [3, 1, 2, 8, 3]
print(plan_operativo(arreglo_L, arreglo_C, 3))

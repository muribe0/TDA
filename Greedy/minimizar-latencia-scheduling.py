"""
Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento,
intentando que se hagan antes del deadline. Una tarea puede completarse luego de su deadline, pero ello
tendra una penalización de latencia. Para este problema, buscamos minimizar la latencia máxima en el que
las tareas se ejecuten. Es decir, dados los arreglos de:

- T tiempo de duraciones de las tareas y D representando al deadline de cada tarea, si definimos que
una tarea i empieza en S_i, entonces termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0)

Nuestra latencia máxima será aquella i que maximice el valor L_i.
Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar
una tarea se puede empezar la siguiente. Indicar y justificar la complejidad del algoritmo implementado.

Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada
tupla indique: (el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
¿Por qué se trata de un algoritmo Greedy? Justificar
"""
# Estrategias a descartar por contraejemplos:
# Deadline menor: ( 2, 2 ) ( 4, 4 ) ( 3, 5 ) -> Optimo -> ( 2, 2 ) ( 4, 4 ) ( 3, 5 ) -> 6
# Tarea de duracion minima: ( 1, 6 ) ( 4, 5 ) -> Optimo -> ( 4, 5 ) ( 1, 6 ) X
# Deadline mayor: ( 10, 11 ) ( 4, 10 ) -> Optimo -> ( 4, 10 ) ( 10, 11 )     X
# Tarea de duracion maxima: ( 2, 2 ) ( 4, 4 ) -> ( 4, 4 ) ( 2, 2 )           X


def minimizar_latencia(D_deadline, T_tareas):
    """
    Este algoritmo funciona si es que los deadlines de cada tarea NO supera el tiempo de la tarea:
    Ejemplo donde puede no funcionar bien: ( 200, 2 ) ( 4, 4 ) ( 3, 5 ) ... Pues 200 >>> 2 de deadline.
    :param D_deadline: lista de deadlines para cada tarea i
    :param T_tareas:  lista de tiempo que toma cada tarea i
    :return: retorna una lista de tuplas del tipo ( tiempo que toma la tarea, latencia de la tarea )
    """
    tareas = [(T_tareas[i], D_deadline[i]) for i in range(len(D_deadline))]
    tareas.sort(key=lambda x: x[1])

    resultante = []
    final = 0
    for tarea in tareas:
        tiempo, deadline = tarea
        resultante.append((tiempo, final + tiempo - deadline if final + tiempo > deadline else 0))
        final = final + tiempo

    return resultante

Deadlines = [2, 4, 5]
Tareas = [2, 4, 3]
print(minimizar_latencia(Deadlines, Tareas))
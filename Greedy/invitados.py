"""
16. El club de Amigos de Siempre prepara una cena en sus instalaciones en la que se desea invitar a la maxima cantidad
de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Solo puede ser invitada
si conoce a al menos 4 personas invitadas.

1. Nos solicitan seleccionar el mayor numero posible de invitados. Proponer una estrategia greedy optima para
resolver el problema
2. Los organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos solicitan que
adicionemos una nueva restriccion a la invitacion: Solo puede asistir si NO conoce al menos otras 4 personas
invitadas. Modifique su propuesta para satisfacer esta nueva solucion.

"""

from grafo import Grafo

def obtener_invitados(conocidos):
    grafo = Grafo()
    for a, b in conocidos: # O(V + E) = O(N)
        if a not in grafo:
            grafo.agregar_vertice(a)
        if b not in grafo:
            grafo.agregar_vertice(b)
        if not grafo.estan_unidos(a, b):
            grafo.agregar_arista(a, b)

    while len(grafo) != 0: # [O(V) * O(V)] + O(V)
        quitar = []
        for v in grafo.obtener_vertices(): # A
            if len(grafo.adyacentes(v)) < 4:
                quitar.append(v)

        if not quitar:
            break

        for v in quitar: # B
            grafo.borrar_vertice(v)

    # B es O(V) total
    # A es O(V) pero se ejecuta V veces. En cambio B es a lo se hace V veces en TOTAL.

    return [v for v in grafo.obtener_vertices()]
import grafo

def es_compatible(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w: continue
            if grafo.hay_arista(v, w):
                return False

def ubicacion(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n: # si tengo un set de n elementos puestos...
        return es_compatible(grafo, puestos)
    if v_actual == len(grafo): # si me pase (ya probe con todos los vertices)...
        return False

    if not es_compatible(grafo, puestos): # Corte "si lo que hice hasta aca, no es compatible, retorno False"
        return False

    # Mis opciones en general son poner o no al vertice en el Set.
    # lo pongo
    puestos.add(vertices[v_actual])
    if ubicacion(grafo, vertices, v_actual + 1, puestos, n): # me fijo si existe solucion compatible que incluya a v_actual
        return True
    else: # si no es compatible, saco al elemento del Set.
        puestos.remove(vertices[v_actual])
        return ubicacion(grafo, vertices, v_actual + 1, puestos, n) # intento con el siguiente vertice la misma estrategia


### ALTERNATIVA

def ubicacion2(grafo, vertices, v_actual, puestos, n):
    if len(puestos) == n: # si tengo un set de n elementos puestos...
        return es_compatible(grafo, puestos)
    if v_actual == len(grafo): # si me pase (ya probe con todos los vertices)...
        return False



    # Mis opciones en general son poner o no al vertice en el Set.
    # lo pongo
    puestos.add(vertices[v_actual])

    if es_compatible(grafo, puestos) and ubicacion2(grafo, vertices, v_actual + 1, puestos, n): # Corte "si lo que hice hasta aca, no es compatible"
        return True

    else: # si no es compatible, saco al elemento del Set.
        puestos.remove(vertices[v_actual])
        return ubicacion2(grafo, vertices, v_actual + 1, puestos, n) # intento con el siguiente vertice la misma estrategia

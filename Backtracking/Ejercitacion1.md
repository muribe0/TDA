# Dominating Set

Un set dominante (Dominating Set) de un grafo F es un subconjunto **D** de vertices de G, tal que para todo vertice de
G:
o bien

i. pertenece a D;

ii. es adyacente a un vertice en D.

Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la minima cantidad de
vertices

![img.png](img.png)

### Estrategia general

1. Si ya encontre solucion, la devuelvo y termino
2. Avanzo si puedo
3. Pruebo si la solucion parcial es valida
    1. Si no lo es, retrocedo y vuelvo a 2.
    2. Si lo es, llamo recursivamente y vuelvo a 1
4. Si llegue hasta aca, ya probe con todo y no encontre una solucion.

1. no queda ninguno por tocar
2. pongo a este,
3. Si este desbloqua, lo incluyo y sigo
4. Si no desbloquea, no lo incluyo y sigo por otro vertice
5. Si llegue hasta aca, no encontre sol

```python


```

## Suma de dados

Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver
todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe
devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. ¿De qué complejidad es el algoritmo en tiempo? ¿Y en espacio?

* Comienza tirando un dado
* Poda: Si la suma de los dados que me quedan por tirar es menor a la suma que me falta, no tiene sentido seguir

```python

def suma(n, s, actual, tirados):
    if sum(tirados) == s:
        return True
    
    if actual + 6 ** n < s:
        return False
    
    for i in range(6, 0, -1):
        tirados.add(i)
        if suman_s(sum(tirados), actual) and suma(n-1, s, actual + i, tirados):
            return True
        else:
            tirados.remove(i)
            break
        

    return False

def sumatoria_dados(n, s):
    tirados = set()
    return []
```
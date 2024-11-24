# Algoritmos Randomizados

* Hacer modelos mas potentes
* Un algoritmo randomizado podria resolver un problema que podria no ser resuelto de forma
  eficiente por un algoritmo determinista
* Conceptualmente son mas sencillos de entender
* Funcionan sin requerir mantener estado interno o memoria del pasado

## Algunos conceptos de Probabilidad

Probabilidad de que un evento ocurra: $P$
Probabilidad de que un evento no ocurra: $1-P$

Ejemplo: lanzar una moneda justa: $P = 0.5$

### Esperanza

Esperanza, valor esperado de un evento: $$E[X] = \sum_{j=0}^{\inf} j \cdot \text{Pr}
[X=j]$$

Esperanza de lanzar una moneda justa: $E[X] = 1 * $

### Problema de Encontrar la Mediana

Para un conjunto de numeros $S = {a_1, a_2, ..., a_n}$, la mediana es el elemento que
estaria en la posicion del medio si el conjunto estuviera ordenado. En especifico:

* si $n$ es impar, la mediana es $a_{(n+1)/2} \rightarrow k = (n+1)/2$
* si $n$ es par, la mediana es $a_{n/2} \rightarrow k = n/2$

Este problema se puede resolver facilmente ordenando. En O(n log n).

Nos gustaria resolverlo en O(n) con un algoritmo randomizado.

#### Problema de seleccion

Para un conjunto de números $S = {a_1, a_2, ..., a_n}$, se quiere seleccionar aquel valor que
estaría en la posición $k$ si el conjunto de números estuviera ordenado.

Se elige algún valor $a_i$, el Pivot. Podemos partir el conjunto de valores en dos
conjuntos, $S^{-}$ con cualquier valor menor a $a_i$, $S^{+}$ con valores mayores a $a_i$
En función de la cantidad de elementos de $S^{-}$ y $S^{+}$, se puede saber dónde buscar
la Selección deseada de $k$

![img.png](img.png)

```python
def select(S, k):
    ai = elegir_pivot(S, k)
    Smenos = [], Smas = []
    for elem in S:
        if elem < ai:
            Smenos.append(elem)
        elif elem > ai:
            Smas.append(elem)

    if len(Smenos) == k - 1: return ai
    if len(Smenos) >= k:
        return select(Smenos, k)
    else:
        return select(Smas, k - len(Smenos) - 1)
```
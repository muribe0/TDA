## Probelma del Viajante por PLE

1. Agregamos virtualmente las aristas faltantes con peso F = "infinito" (=sumatoria de todas las aristas existentes + 1)
2. Vamos a construir nuestras variables Y$_{i,i} = 1$ si usamos la arista i -> j (0 sino).
3. $\sum_i Y_{i,j}$

Agregamos una variable $p_i$: numero de secuencia en la cual visito a la ciudad i.

## Vertex Cover

* $Y_i$: El vertice $i$ se encuentra en el VC. si $$\forall (v,w)\in E : Y_v + Y_w \geq 1$$
* min $\sum_i Y_i$

Mejorar el modelo:
> Si un vertice no esta en el conjunto, entonces todos sus adyacentes deben estar en el conjunto.

$\forall i \in V:$ $$ Y_i + \sum_{j\in ady(i)} Y_k \geq len(ady(i)) \cdot (1-Y_i)$$

$(1-Y_i) = 1$ si $i$ no esta en el VC. $0$ si $i$ esta en el VC.

## FLujo Maximo

* $\sum_{v\in V} f^{in}(v) = \sum_{v\in V} f^{out}(v)$ para todo vertice $v$.
* $f(e) \leq c(e)$ para todo eje $e$.
* $f^{in}(s) = 0$ y $f^{out}(t) = 0$.
* $max \Big(\sum_{v\in V} f^{in}(f) \Big)$

$f$ : flujo que consume / pasa por el eje.


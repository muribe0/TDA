
Reglas de greedy
* Aplicamos una regla sencilla que nos permita obtener el optimo local a mi estado actual.
* Aplicamos iterativamente esa regla, esperando que nos lleve al optimo general (la mejor solucion).
* No siempre dan un resultado optimo
* Demostrar  que dan un resultado optimo es dificil
* Son faciles de pensar
* Suelen funcionar rapido
* Para problemas *complejos* pueden ser buenas aproximaciones.

Ejemplos:
### Dijkstra
Encuentra el camino minimo en un grafo pesado con pesos positivos.
1. Va eligiendo el vertice con menor distancia en cada paso. 
```
function Dijkstra(Graph, source):
    dist[source] = 0
    for each vertex v in Graph:
        if v ≠ source
            dist[v] = infinity
        prev[v] = undefined
    
    Q = set of all vertices in Graph
    
    while Q is not empty:
        u = vertex in Q with minimum dist[u]
        remove u from Q
        
        for each neighbor v of u:
            alt = dist[u] + length(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    
    return dist[], prev[]
```
### Kruskal
Encuentra el MST
1. Ordena las aristas de menor a mayor peso
2. Elije siempre las primeras aristas (u,v) con menor peso para $u,v \in V$
### Prim
Encuentra el MST
1. Entre las aristas visibles, agrega siempre la menor hasta incluir todas con un solo camino

Tengo un aula donde quiero dar charlas. Las charlas tienen horario de inicio y fin. Quiero utilizar el aula para dar la mayor cantidad de charlas.

![[Pasted image 20240829201351.png]]

```python
def scheduling(horarios):
	 horraios_ordenados = ordenar_por_horario_fin(horarios)
	 charlas = []
	 for horario in horarios_ordenados:
		 if len(charlas) == 0 or not hay_interseccion(charlas[-1], horario):
			 charlas.append(horario)
	 return charlas
```

## Arboles de Huffman
Huffman plantea una forma de comprimir un texto en base a la frecuencia de los caracters en el mismo.
Utiliza un heap (de minimos) de forma auxiliar para ir generando el arbol de codigos.

### P A R A L E L A M E N T E 
| P   | A   | R   | L   | E   | M   | N   | T   | total |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- |
| 1   | 3   | 1   | 2   | 3   | 1   | 1   | 1   | 13    |
El heap de minimos va desencolando las letras con menor frecuencia. La P, R, M, N y T van a salir antes que el resto.

### Problema del cambio
Elegir el billete de mayor denominacion no siempre es optimo.
para billetes de denominacion [1, 5, 6, 9] no va a ser optimo si quiero cambio de 11, por ejemplo.

### Problema de compras con inclacion
| 0   | 1   | 2   | 3    | 4   |
| --- | --- | --- | ---- | --- |
| $32 | $21 | $87 | $100 | $15 |
Cada dia hay que comprar un producto y solo uno, pero los precio aumentan todo el tiempo
El precio del producto $i$ el dia $j$ = $R[i]^{j+1}$ con $j = {0,1..}$

Sol: Agarrar los que tengan mayor precio primero
Optimizacion: ordenarlos por mayor precio

### Problema de la carga de combustible

Un camión debe viajar desde una ciudad a otra deteniéndose a cargar combustible para poder llegar a destino. El tanque de combustible le permite viajar hasta K kilómetros.

Las estaciones se encuentran distribuidas a lo largo de la ruta siendo di la distancia desde la estación i-1 a la estación i.

1. Implementar un algoritmo que decida en qué estaciones conviene detenerse a cargar combustible, de manera que se detenga la menor cantidad de veces posible.
    
2. Indicar y justificar la complejidad del algoritmo.

Sol: aplazo lo mas que puedo la carga de tanque, encontrando a la estacion j que este a mayor dist desde mi ubicacion.
Entonces K tiene que ser mayor o igual a la suma de distancias desde mi posicion actual hasta la estacion j. Repetir.

# Greedy parte 2
Problema de la mochila
* Capacidad: $W$
* Tengo elementos a guardar. Cada uno con $k_i$ valor y $w_i$ peso.

Idea 1) Mayor a menor valor
Contra ejemplo: 

|       | 1   | 2   | 3   |
| ----- | --- | --- | --- |
| Peso  | 10  | 9   | 1   |
| Valor | 5   | 10  | 7   |


Idea 3) Ordenar de mayor a menor relacion $\frac{v}{w}$

|       | 1   | 2   | 3   | 4   |
| ----- | --- | --- | --- | --- |
| Peso  | 5   | 3   | 1   |     |
| Valor | 10  | 6   | 7   |     |
### Scheduling
Ahora tenemos tareas con un deadline (fecha límite) di y una duración ti, pero pueden hacerse en cualquier momento, siempre que se hagan antes del deadline. Si se hacen después del deadline, incurrimos en una latencia. 

Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. Es decir, si definimos que una tarea i empieza en si, entonces termina en fi = si + ti, y su latencia es li = fi - di (si fi > di, sino 0).

Sol: Hacer primero las tareas con un deadline mas proximo.

### Grafo
Dado una lista de n números naturales, implementar un algoritmo en tiempo polinomial que cree un grafo de n nodos cuyos grados sean los indicados por esa lista. G debe ser simple y si bucles.

1. Ordenamos de may a menor grado
2. Uno al de menor con el de mayor grado
3. Mientras tanto, les resto uno a cada nodo afectado en la lista de numeros
4. Aplicandolo n veces, si hay solucion, la va a encontrar. (es optimo)
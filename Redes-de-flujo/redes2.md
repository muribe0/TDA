Dado un grafo no dirigido, un match es un subconjunto de las aristas en el cual para todo vértice V a lo sumo una arista
del match incide en V (en el match, tienen grado a lo sumo 1). Decimos que el vértice v está matcheado si hay alguna
arista que incida en él (sino, está unmatcheado). El matching máximo es aquel en el que tenemos la mayor cantidad de
aristas (matcheamos la mayor cantidad posible).

> Problema: Dado cualquier grafo bipartito, encontrar el mejor matching.

Sea G el grafo bipartito.

```mermaid
graph LR
    A(A)
    B(B)
    C(C)
    D(D)
    E(E)
    F(F)
    G(G)
    A --> E
    B --> D
    B --> E
    B --> F
    C --> F
    C --> G
```

Pasos para resolver:

1. Se crea un nuevo grafo agregando dos nodos s y t.
2. Se le coloca a todas las aristas un peso de 1.
3. Luego, se le aplica el algoritmo de Ford Fulkerson.
4. Se obtiene el matching máximo. Siendo $k = |f|$ la cantidad de aristas en el matching, entonces $k$ es el matching
   máximo.

```mermaid
graph LR
    A(A)
    B(B)
    C(C)
    D(D)
    E(E)
    F(F)
    G(G)
    t(t)
    s -->|1| A
    s -->|1| B
    s -->|1| C
    A -->|1| E
    B -->|1| D
    B -->|1| E
    B -->|1| F
    C -->|1| F
    C -->|1| G
    D -->|1| t
    E -->|1| t
    F -->|1| t
    G -->|1| t
```

Con Ford Fulkerson tenemos tipicamente a $O(E \cdot V^2)$. Pero

## Caminos disjuntos

Decimos que dos caminos son disjuntos si no comparten aristas (pueden compartir nodos).
Dado un grafo dirigido y dos vértices s y t, encontrar el máximo número de caminos disjuntos s-t en G.
Pro-tip: recuerden cómo funciona FF

```mermaid
graph LR
    s(s)
    A(A)
    B(B)
    C(C)
    D(D)
    E(E)
    t(t)
    s -->|1| A
    s -->|1| B
    A -->|1| D
    B -->|1| D
    C -->|1| E
    s -->|1| C
    D -->|1| t
    E -->|1| t
```

Puedo usar FF para encontrar caminos disjuntos de forma progresiva. EN cada iteracion se encuentra el camino mas cercano
progresivamente usando BFS-FF. Luego, se bloquean (o *eliminan*) las aristas de ese camino y se vuelve a buscar otro
camino.

## Caminos disjuntos no dirigidas

Para caminos disjuntos no dirigidos, se fuerza al grafo a ser dirigido mientras sigue cumpliendo con las antiparalelas.

Del grafo:

```mermaid
graph LR
    s(s)
    A(A)
    B(B)
    C(C)
    D(D)
    E(E)
    t(t)
    s ---|1| A
    s ---|1| B
    A ---|1| D
    B ---|1| D
    C ---|1| E
    s ---|1| C
    D ---|1| t
    E ---|1| t
```

Paso a:

Estrategia:
S para por algun vertice `u` aprovechando el camino de `u`->`v`.

## Circulaciones con demandas

Supongamos que tenemos varias "fuentes" con un suministro, y "sumideros" con una demanda. Ahora cada nodo tiene una
demanda (positiva, negativa o 0).

En grafos normales, **sin demanda**, teniamos que $f_{in}(v) - f_{out}(v) = 0$. Ahora deciemos que para grafos con
demandas, puede ocurrir que el nodo `u` tenga:
$f_{in}(u) - f_{out}(u) = d$. Lo que aparece dentro de cada nodo es lo que quiere consumir. Si aparece negativo, es
porque lo produce.

> A produce 3. Los que tengan demanda negativa producen.

Nuevas condiciones

1. $0 \leq f(e) \leq c_e$ : el flujo de un eje esta acotado por su capacidad
2. $f_{in}(u) - f_{out}(u) = d$ : la demanda de un nodo es igual a la suma de lo que entra menos lo que sale.

```mermaid 
graph LR
    A("-3") -->|2| C(2)
    A -->|1| B("-3") -->|2| C
    B -->|2| D(4)
    C -->|2| D
```

Podemos re-escribir el grafo de la siguiente forma:

1. Agregando un nodo `s` que va a ser la fuente de los nodos con demanda negativa. Este supor nodo `s` tiene como
   finalidad generar esa demanda que generaban los nodos con demanda negativa.
2. Agregando un nodo `t` que tiene como finalidad absorber la demanda de los nodos con demanda positiva.
3. Dejando las capacidades intactas.

```mermaid
graph LR
    s --> |3|A -->|3| C
    A --> |3|B -->|2| C
    s --> |3|B -->|2| D
    C --> |2|D --> |2|t
    C --> |2|t
```

Finalmente, se puede aplicar el algoritmo de FF para encontrar la circulación máxima.

## Ejercicio

Supongamos que tenemos un sistema de una facultad en el que cada alumno puede pedir hasta 10 libros de la biblioteca. La
biblioteca tiene 3 copias de cada libro. Cada alumno desea pedir libros diferentes. Implementar un algoritmo que nos
permita obtener la forma de asignar libros a alumnos de tal forma que la cantidad de préstamos sea máxima.

Modelo diciendo que cada libro puede ser prestado a lo sumo 3 veces. Cada alumno puede pedir hasta 10 libros. Cada libro
puede ser prestado a un alumno puntual 1 sola vez.

```mermaid
graph LR
    s -->|3| L1 -->|1| A2 -->|10| t
    s -->|3| L2 -->|1| A3 -->|10| t
    s -->|3| L3 -->|1| A1 -->|10| t
    L3 -->|1| A2
    L3 -->|1| A3
```

Alternativa:

```mermaid
graph LR
    s -->|10| A1 -->|1| L2 -->|3| t
    s -->|10| A2 -->|1| L3 -->|3| t
    s -->|10| A3 -->|1| L1 -->|3| t
    A3 -->|1| L2
    A1 -->|1| L1
    A2 -->|1| L1
```

Un grafo G tiene una circulación factible con demandas sii para todos los cortes (A, B):
$$
\sum_{v \in B} d_v \leq c(A,B)
$$

## Circulacion con demandas y cotas minimas
Ahora para cada arista, ademas de tener una capacidad tenemos una cota inferior que **debe** cumplirse.

Nuevas condiciones

1. $L_e \leq f(e) \leq c_e$ : el flujo de un eje esta acotado por su capacidad y cota minima.
2. $f_{in}(u) - f_{out}(u) = d$ : la demanda de un nodo es igual a la suma de lo que entra menos lo que sale.

Dado un grafo G con demandas y cotas minimas, se puede:
1. Hacer que la demanda del vertice $v$ sea $d + L_{(u,v)}$. Es decir, hacer que la demanda de un vertice sea la
   demanda original mas la cota minima de la arista que lo conecta con el vertice $v$.
2. Agregar un nodo `s` que va a ser la fuente de los nodos con demanda negativa. Este supor nodo `s` tiene como
   finalidad generar esa demanda que generaban los nodos con demanda negativa.
3. Agregar un nodo `t` que tiene como finalidad absorber la demanda de los nodos con demanda positiva.


### Ejemplo: Diseño de encuestas

Suponer que tenemos una empresa que vende $k$ productos y tenemos el historial de compras de cada cliente. QUeremos enviar encuestas a $n$ clientes para averiguar cuales son los productos que mas les gusta.

Consideraciones:
1. Cada cliente sera consultado por un subset de productos (y siempre que el/ella hayan comprado).
2. La cantidad de preguntas a un cliente $i$ debe estar entre algun rango.
3. Para cada producto $j$ deben haver entre $P_j$ y $P_j '$ preguntas.

![img_7.png](img_7.png)

Ejemplo:

```mermaid
graph LR
    s --> |"c2,c2'"|c2 --> |1| p1 & p2 & p3
    s --> |"c1,c1'"|c1 --> |1| p1 & p2
    s --> |"c3,c3'"|c3 --> |1| p2 & p3
    
    p1 --> |"P1,P1'"| t
    p2 --> |"P2,P2'"| t
    p3 --> |"P3,P3'"| t
```
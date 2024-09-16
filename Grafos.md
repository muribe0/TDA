Grafo: TDA con entidades
Tipos:
* Pesados, no pesados
* Dirigidos, no dirigidos

Conectividad
* Grafos no dirigidos -> Componentes conexas
* Grafos dirigidos -> Componentes fuermenete conexas (y debilmente)

Orden Topologico
Un orden topológico de un grafo dirigido acíclico es una ordenación lineal de sus vértices tal que, para cada arista dirigida de u a v, u aparece antes que v en la ordenación.

Grafos bipartitos
Puedo partirlo en 2 subconjuntos A y B. Donde todos los $v \in A$ solo tienen aristas con otros vertices de A.

Arboles de tendido minimo
Subconjunto de aristas tales que todos los vertices se mantengan conexos, sin ciclos y la suma de todas las aristas de G' resulte minima.

Representaciones:
* Matriz de adyacencia
* Lista de adyacencia

Propiedades matematicas de la matriz de adyacencia
Lo obvio:
* $V \times V$
* Si es no dirigido, la matriz es simetrica
* Si no hay bucles, la diagonal son todos ceros

Teorema: Potenciacion de la MA
Siendo A la matriz de adyacencia de un grafo G -> $A^n_{ij}$ nos indica la cantidad de caminos de largo $n$ de $i$ a $j$.

Demostramos por induccion:
1. Vale para caso inicial ($A^1$)?
2. Si vale para $A^n$, vale para $A^{n+1}$

Paso inductivo
Suponemos que tenemos una matris $F^n$ que nos indica la cantidad de caminos que hay entre i y j de largo n en el grafo G.
Si la propiedad vale para $A^n$ => $F^n = A^n$

Podemos expresar un camino de n+1 de i a j como los caminos de largo $n$ de i a k, y luego un camino de largo 1 de $k$ a $j$.

![[Pasted image 20240822205035.png]]

$A_{kj}$ es el valor de camino de k a j, si es que existe

## Handshaking Lemma
En todo grafo no dirigido, la cantidad de vertices con un grado impar, es par.

$$\sum\limits_{v}^{} grado(v) = 2E$$
$$\sum\limits_{v}^{} grado(v) = \sum\limits_{v-impar}^{} grado(v) + \sum\limits_{v-par}^{} grado(v)$$
$$\sum\limits_{v-impar}^{} grado(v) + \sum\limits_{v-par}^{} grado(v) = 2E$$

Ambas sumatorias tienen y deben ser pares.

### Un grafo es bipartito sii no tienen ciclos impares
Si es bipartito -> o tiene ciclos impares: metodo directo


## Graph coloring

Thm: if every node in the graph G has degree at most **d**. Then this basic algorithm uses at most $d+1$ colors for G.

Proof: Induction
Base case: n = 1 => 0 edgees:
* d is 0
* 1 color = d + 1  
Induction step: Assume $P(n)$ is true for the induction. Let G = (V, E) be any n+1 node graph. Let d be the max degree in G.
1. Order the nodes some arbitrary way / $v_1, v_2, \dots v_n, v_{n+1}$.
2. Remove $v_{n+1}$ from G to create $G'=(V',E')$.
3. $G'$ has max degree $\leq$  d and n nodes so P(n) says Basic Algorithm uses $\leq$ d+! colors for $v_1, v_2, \dots v_n$
4. $v_{n+1}$ has at most d neighbors => There exist at leas one color in the set $\{c_1, c_2, \dots , c_d+1\}$ => Basic Algorithm uses at most d+1 colors. 
Therefore, the induction is complete and the Thm is true.

Def: A graph G is bipartite if V can be split into $V_L$ and $V_R$ so thta all the edges connect a node in $V_L$ to a node in $V_R$.
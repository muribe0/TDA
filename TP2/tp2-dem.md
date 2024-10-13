### Definiciones:

Sea $M = \{m_1, m_2, ..., m_n\}$ un conjunto de $n$ monedas con valores distintos y desordenados.

Definimos $S \in \mathbb{R}_{n\times n}$ asociada al arreglo de $n$ monedas desordenadas no repetidas.
Definimos $m_i$ como la moneda $i$ y $m_j$ como la moneda $j$ del arreglo, con $1 \leq i \leq j \leq n$.
Asociamos  $k = j - i + 1$ al largo del subarreglo de monedas $\{m_r \in M : \forall r \in [i,j]\}$.

**Optimalidad**: Consideraremos a solución óptima si y solo si maximiza la suma de los valores de las monedas que Sophia
puede obtener, considerando la estrategia _greedy_ de Mateo.

Notamos que el algoritmo construye la matriz columna por columna, con $j$ tomando los valores
ordenados $\{1, 2, \dots, n\}$
e $i$ tomando $\{j, j-1, \dots, 1\}$. De esta manera, se garantiza que al momento de llegar a un instante
del algoritmo donde el subproblema con valores $a,b$ quieren ser calculados: $S_{x,y}$ haya sido calculado para
todo $x \in \{a, a-1, \dots, 1\}$ y
todo $y \in {1, 2, \dots, b}$ con $x \neq a \vee y \neq b$. Esto es importante debido a que algunos de esos valores ya
calculados serviran para hallar $S_{a,b}$.

### Hipótesis:

El algoritmo en la función `juego(monedas)` calcula $S_{i, j}$ para todo $1 \leq i \leq j \leq n$, donde $S_{1,n}$
representa el valor máximo que Sophia puede acumular en el juego completo.

### Tesis:

$\forall i,j \in \mathbb{N}, 1 \leq i \leq j \leq n: S_{i, j}$ es el valor óptimo para el subarreglo $[i,j]$.

### Paso Inductivo:

**Caso Base**: $k = 1$ (una sola moneda)
$S_{i, j} = m_i$, que ocurre cuando Sophia elije la única moneda.

Sea $S_{i, j} = \max\{m_i + S_{i',j'}, m_j + S_{i'',j''}\}$, donde:

- Si Sophia elige $m_i$ (a Mateo le queda la segunda o última moneda):
    - Si $m_{i+1} > m_j$, entonces $i' = i+2, j' = j$
    - Si $m_{i+1} \leq m_j$, entonces $i' = i+1, j' = j-1$
- Si Sophia elige $m_j$ (a Mateo le queda la primer o ante-última moneda):
    - Si $m_i > m_{j-1}$, entonces $i'' = i+1, j'' = j-1$
    - Si $m_i \leq m_{j-1}$, entonces $i'' = i, j'' = j-2$

1. Las soluciones para los subarreglos $[i',j']$ y $[i'',j'']$ ya han sido calculadas y tienen tamanio menor a $k$.
2. Por hipótesis inductiva, si $S_{i',j'}$ y $S_{i'',j''}$ son óptimos, $S_{i, j}$ **es óptimo**.

**Prueba por Contradicción**:

Supongamos que existe una estrategia **alternativa** $S'_{i,j} > S_{i,j}$.

1. Sophia debe elegir entre $m_i$ o $m_j$.
2. Caso 1: Si $S'_{i,j}$ comienza eligiendo $m_i$:

   * Entonces $S'_{i,j} = m_i + S'_{i',j'}$, donde $[i',j']$ es el subarreglo resultante después de que Mateo elige su moneda
     según su estrategia greedy y según, la hipótesis $S'_{i,j} > S_{i,j}$ .Pero sabemos que si $S_{i',j'}$ es óptimo para el subarreglo $[i',j']$, $S'_{i',j'} \leq S_{i',j'}$. 
   * Esto implica que $S'_{i,j} = m_i + S'_{i',j'} \leq m_i + S_{i',j'} \leq S_{i,j}$, ya que $S_{i,j}$ considera esta opción
     en su cálculo de máximo.

3. Caso 2: Si $S'_{i,j}$ comienza eligiendo $m_i$:

   * Entonces $S'_{i,j} = m_j + S'_{i'',j''}$, donde $[i'',j'']$ es el subarreglo resultante después de que Mateo elige su moneda
     según su estrategia greedy y según, la hipótesis $S'_{i,j} > S_{i,j}$. Pero sabemos que si $S_{i'',j''}$ es óptimo para el subarreglo $[i'',j'']$, $S'_{i'',j''} \leq S_{i'',j''}$.
   * Esto implica que $S'_{i,j} = m_j + S'_{i'',j''} \leq m_j + S_{i'',j''} \leq S_{i,j}$, ya que $S_{i,j}$ considera esta opción
     en su cálculo de máximo.

Por lo tanto, $S'_{i,j} = \max\{m_i + S'_{i',j'}, m_j + S'_{i'',j''}\} \leq S_{i,j}$.

**Conclusión**:

Por el principio de inducción, $S_{i, j}$ es óptimo para todo subarreglo $[i,j]$, $1 \leq i \leq j \leq n$.
En particular, $S(1,n)$ es el valor óptimo para el juego completo.



### LATEX OVERLEAF


\section{Optimalidad}

\subsection{Definiciones}

Sea $M = \{m_1, m_2, ..., m_n\}$ un conjunto de $n$ monedas con valores distintos y desordenados.

Definimos $S \in \mathbb{R}_{n\times n}$ a la matriz asociada al problema. Definimos $m_i$ como la moneda $i$ y $m_j$ como la moneda $j$ del arreglo, con $1 \leq i \leq j \leq n$.
Asociamos  $k = j - i + 1$ al largo del sub-arreglo de monedas $\{m_r \in M : \forall r \in [i,j]\}$.

\textbf{Optimalidad}: Consideraremos a solución óptima si y solo si maximiza la suma de los valores de las monedas que Sophia
puede obtener, considerando la estrategia \textit{greedy} de Mateo.

Notamos que el algoritmo construye la matriz columna por columna, con $j$ tomando los valores
ordenados $\{1, 2, \dots, n\}$
e $i$ tomando $\{j, j-1, \dots, 1\}$. De esta manera, se garantiza que al momento de llegar a un instante
del algoritmo donde el subproblema con valores $a,b$ quieren ser calculados: $S_{x,y}$ haya sido calculado para
todo $x \in \{a, a-1, \dots, 1\}$ y
todo $y \in {1, 2, \dots, b}$ con $x \neq a \vee y \neq b$. Esto es importante debido a que algunos de esos valores ya
calculados servirán para hallar $S_{a,b}$.

\subsection{Hipótesis}

El algoritmo calcula $S_{i, j}$ para todo $1 \leq i \leq j \leq n$, donde $S_{1,n}$
representa el valor máximo que Sophia puede acumular en el juego completo.

\subsection{Tesis}

$\forall i,j \in \mathbb{N}, 1 \leq i \leq j \leq n: S_{i, j}$ es el valor óptimo para el subarreglo $[i,j]$.

\subsection{Paso inductivo}

\textbf{Caso Base}: $k = 1$ (una sola moneda)
$S_{i, j} = m_i$, que ocurre cuando Sophia elije la única moneda.

Sea $S_{i, j} = \max\{m_i + S_{i',j'}, m_j + S_{i'',j''}\}$, donde:
\begin{itemize}
\item Si Sophia elige $m_i$ (a Mateo le queda la segunda o última moneda):
\begin{itemize}
\item Si $m_{i+1} > m_j$, entonces $i' = i+2, j' = j$
\item Si $m_{i+1} \leq m_j$, entonces $i' = i+1, j' = j-1$
\end{itemize}
\item Si Sophia elige $m_j$ (a Mateo le queda la primer o ante-última moneda):
\begin{itemize}
\item Si $m_i > m_{j-1}$, entonces $i'' = i+1, j'' = j-1$
\item Si $m_i \leq m_{j-1}$, entonces $i'' = i, j'' = j-2$
\end{itemize}
\end{itemize}

\begin{enumerate}
\item Las soluciones para los subarreglos $[i',j']$ y $[i'',j'']$ ya han sido calculadas y tienen tamanio menor a $k$.
\item Por hipótesis inductiva, si $S_{i',j'}$ y $S_{i'',j''}$ son óptimos, $S_{i, j}$ \textbf{es óptimo}.
\end{enumerate}

\subsection{Prueba por Contradicción}

Supongamos que existe una estrategia \textbf{alternativa} $S'_{i,j} > S_{i,j}$.

\begin{enumerate}
\item  Sophia debe elegir entre $m_i$ o $m_j$.
\item  Caso 1: Si $S'_{i,j}$ comienza eligiendo $m_i$:    
\begin{itemize}
\item  Entonces $S'_{i,j} = m_i + S'_{i',j'}$, donde $[i',j']$ es el subarreglo resultante después de que Mateo elige su moneda según su estrategia greedy y según, la hipótesis $S'_{i,j} > S_{i,j}$ .Pero sabemos que si $S_{i',j'}$ es óptimo para el subarreglo $[i',j']$, entonces $S'_{i',j'} \leq S_{i',j'}$.
\item Esto implica que $S'_{i,j} = m_i + S'_{i',j'} \leq m_i + S_{i',j'} \leq S_{i,j}$, ya que $S_{i,j}$ considera esta opción en su cálculo de máximo.
\end{itemize}
\item Caso 2: Si $S'_{i,j}$ comienza eligiendo $m_i$:
\begin{itemize}
\item  Entonces $S'_{i,j} = m_j + S'_{i'',j''}$, donde $[i'',j'']$ es el subarreglo resultante después de que Mateo elige su moneda según su estrategia greedy y según, la hipótesis $S'_{i,j} > S_{i,j}$. Pero sabemos que si $S_{i'',j''}$ es óptimo para el subarreglo $[i'',j'']$, entonces $S'_{i'',j''} \leq S_{i'',j''}$.
\item  Esto implica que $S'_{i,j} = m_j + S'_{i'',j''} \leq m_j + S_{i'',j''} \leq S_{i,j}$, ya que $S_{i,j}$ considera esta opción en su cálculo de máximo.
\end{itemize}
\end{enumerate}

Por lo tanto, $S'_{i,j} = \max\{m_i + S'_{i',j'}, m_j + S'_{i'',j''}\} \leq S_{i,j}$.

\subsection{Conclusión}

Por el principio de inducción, $S_{i, j}$ es óptimo para todo subarreglo $[i,j]$, $1 \leq i \leq j \leq n$.
En particular, $S(1,n)$ es el valor óptimo para el juego completo.
Para cada moneda,
cuando le toca a sophi: agarrar la de mayor denominacion
cuando le toca a marcos: agarrar la de menor denominacion

Dado un arreglo de n monedas, y R el arreglo ordenado con cada moneda obtenida, donde los r_i son las monedas y
las i pares o cero son de Sophi, las i impares son de Marcos.
Se sabe que:

* $m_0 >= m_1$ ->   $m_0 - m_1$= `ventaja` $>= 0$
* $m_2 >= m_3$ -> `ventaja_ant` + `ventaja` $>= 0$
* ...
* $m_k$ >= $m_{k+1}$ -> ventaja ya es cero o mas + nueva ventaja >= 0

por lo que queda demostrado que Sophi siempre obtendra una ventaja positiva o nula frente a su hermano.
from random import randint

### Demostración

Sea $C$ el arreglo de $n$ monedas y `S` el arreglo de monedas de Sophi, `M` el arreglo de monedas de Marcos.
Se tiene que $s_i$ corresponde a la moneda $i$ de Sophi y $m_i$ a la de Mateo para $i \in N_0$.

Luego, definimos $v_i : \text{ventaja}$ como $v_i = s_i - m_i$ donde se sabe que $s_i \geq m_i$ para todo $i$. Por lo que 
sigue que $v_i \geq 0$ para todo $i$. 

Por lo tanto la diferencia (ventaja) total $V$ que tendrá Sophi al final del juego se obtiene por
$$
V = \sum_{i=0}^k v_i 
$$
donde $k = \lfloor\frac{n}{2}\rfloor $. Si $n$ es impar:
$$
V = v_{k+1} + \sum_{i=0}^k v_i
$$

Finalmente, como cada ventaja $v_i \geq 0$, se tiene que $V \geq 0$ para cualquier arreglo de tamanio $n \in N$. Por lo tanto, queda demostrado que  
el algoritmo es óptimo en encontrar el escenario donde Sophi gana siempre (o empata en caso de un arreglo par equilibrado).

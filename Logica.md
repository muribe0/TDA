H -> T "Si H, entonces T"
Si H es falsa, la implicacion es verdadera (no importa el valor de T)
Si T es verdadera, la implicacion es verdadera (no importa el valor de H)
Si H es verdadera, entonces T debe ser verdadera.

$H \rightarrow T = ~H \vee (H  \wedge T)$

## Metodo directo
Asumimos que la hipotesis es verdadera, y demostramos que la tesis tambien lo es.

n es impar -> n^2 es impar
Suponemos que la hipotesis es verdadera y por cuentas matematicas llegas a la tesis.
H -> T

## Metodo del contrarreciproco
Demostramos que ~T -> ~H, por metodo directo. Ejemplo:

$a \cdot b$  es par -> $a$ es par $\vee$ $b$ es par
Supongamos que la tesis es falsa (ambos son impares) ...![[Pasted image 20240822202153.png]]

=> $a \cdot b$ es impar

Por el absurdo/contradiccion
Asumimos que la hipotesis es verdadera y la tesis es falsa, y llegamos a una contradiccion (en el sentido logico). Ejemplo:

![[Pasted image 20240822202517.png]]

![[Pasted image 20240822203022.png]]

Si vale para h, vale para h+1. Por lo que caen por efecto domino todos los valores.


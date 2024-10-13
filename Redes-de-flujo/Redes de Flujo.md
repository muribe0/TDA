# Redes de flujo

* Podemos modelar con grafos flujos de materiales (ej cloacas, información en redes).
* El grafo es dirigido.
* Tenemos una (única) fuente, y un (único) sumidero ( → una única componente débilmente conexa). Fuente: vértice con grado de entrada 0. Sumidero: vértice de grado de salida 0.
* Cada vértice intermedio simplemente traslada lo que le pasan. No produce ni consume. → Conservación de la materia, energía, carga eléctrica, etc...
* Cada arista tiene un peso que refleja la capacidad de transporte por esa vía. 

```mermaid

graph
    s --> B
    s --> A
    A --> D
    B --> C
    C --> D
    D --> t
    B --> t
    
```


![img.png](img.png)

## Restricciones
1. No se aceptan bucles
2. No pueden haber ciclos de 2 vertices
3. Solo debe haber una fuente y un sumidero

### 1. Si hay bucles: los sacamos
### 2. Si hay ciclos de 2 vertices: los convierto
![img_1.png](img_1.png)
### 3. Si hay más de una fuente o sumidero: los convierto
![img_2.png](img_2.png)

Red residual
* Tendra los mismos vertices que la red original
* Tendra las mismas aristas, con la capacidad que les quede (inicia en w(A,B)).
* Tendra aristas inversas, con la capacidad que se haya usado (inicia en 0)

## Algoritmo de Ford-Fulkerson
Si encontramos un camino de la fuente al sumidero en la red residual, entonces encontramos un camino por el que podemos aumentar el flujo.

## Corte minimo
El corte minimo de una red es la suma de los pesos de las aristas que al eliminarlas, desconectan la fuente del sumidero.
Si el grafo es no pesado, puedo considedar a todas las aristas con peso 1. Por lo que el corto minimo es la cantidad de aristas que desconectan la fuente del sumidero.

Esto aplica a cualquier tipo de grafo

Corte minimo en este recorrido: 9

![img_3.png](img_3.png)

## Teorema de max-flow min-cut
Si el grafo corresponde a una red de flujo, entonces el flujo máximo es igual al corte mínimo.


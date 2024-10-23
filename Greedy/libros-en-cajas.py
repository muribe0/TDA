"""
Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros).
Tu objetivo es guardar esos libros en la menor cantidad de cajas. Todas las cajas disponibles son de la misma
capacidad L (se asegura que L >= n). Obviamente, no podés partir un libro para que vaya en múltiples cajas,
pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L.
Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar.
Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.
¿El algoritmo propuesto encuentra siempre la solución óptima? Justificar.
¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros?
Describir cómo afecta a la complejidad,y a su optimalidad.
"""

# Se sabe que pueden entrar todos y queremos minimizar la cantidad de cajas usadas
# Idea: Colocar primero los libros de mayor espesor.
# Esto se hace de la siguiente manera:
# Coloca un libro en un caja A.
# 1. Si hay espacio para el siguiente, colocalo en A
# 2. Si no hay espacio, colocalo en otra caja B.
# Asi hasta acabar con los libros.

# Funciona porque, de existir alguna caja A' donde colocar, se va a colocar ahi.
# Si se crea una caja B es porque no existe caja actual que pueda almacenar

"""
# Demostración de Optimalidad del Algoritmo Greedy para Empaquetamiento de Libros

## Teorema
El algoritmo greedy que ordena los libros de mayor a menor espesor y los coloca en la primera caja disponible es óptimo para el problema de empaquetamiento de libros.

## Demostración por Contradicción

### Supuesto
Supongamos, por contradicción, que existe una solución óptima que utiliza menos cajas que la solución proporcionada por nuestro algoritmo greedy.

### Paso 1: Análisis de la solución greedy
Sea G = {G₁, G₂, ..., Gₖ} la solución greedy, donde cada Gᵢ es una caja.

### Paso 2: Análisis de la supuesta solución óptima
Sea O = {O₁, O₂, ..., Oₘ} la supuesta solución óptima, donde m < k.

### Paso 3: Comparación de soluciones
Consideremos el libro más grueso en la solución greedy que está en una caja diferente en la solución óptima. Llamemos a este libro L.

### Paso 4: Análisis del libro L
- En la solución greedy, L está en una caja Gᵢ.
- En la solución óptima, L está en una caja Oⱼ.

### Paso 5: Contradicción
Si L está en Oⱼ en lugar de una caja anterior en la solución óptima, entonces todos los libros en las cajas O₁, O₂, ..., Oⱼ₋₁ deben ser más gruesos que L.

Pero esto contradice nuestra suposición de que L es el libro más grueso que está en una caja diferente en la solución óptima.

### Conclusión
Por lo tanto, nuestra suposición de que existe una solución óptima que utiliza menos cajas que la solución greedy debe ser falsa.

## Corolario
El algoritmo greedy produce una solución óptima para el problema de empaquetamiento de libros.
"""

import math

def cajas(capacidad, libros):
    libros.sort(reverse=True)
    capacidades = []
    cajass = []

    for libro in libros:
        for i in range(len(capacidades)):
            if libro <= capacidades[i]:
                capacidades[i] -= libro # meto el libro en una caja existente, si entra
                cajass[i].append(libro)
                break
        else:
            capacidades.append(capacidad - libro) # sino, creo una nueva caja y lo meto ahi
            cajass.append([libro])
    return cajass

print(cajas(5, [2.3,2.2,math.pi, 1.941234, 1/2, 4.99999, 5.0, 0.2, 0.111111]))

# Funciona porque:
### Sudoku
Mejoras para sudoku:
* Optimizar calculando de antemano las posibilidades para cada casillero.
* Calcular primero los casilleros donde hay menos alternativas, esperando generar un efecto domino que reduzca las alternativas de los siguientes.

### Caballo

![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeO9OhT5ZqOwWvm0Jz_t-tWJ9lMEVXUqOfIBSKPnveNkMjJDlEsMITcBDp5gGxMLxvW53khznVuBz_lXdyQHBMRYfsroUPCo8qgXJ5KycWdkTkVsD552oI1kI8-n-aBJgAoqJ4SoKoryzzFxLfW_4k02Pr2gGQ=s2048?key=gKqW96ITNxjx2HmFvGD60A)


Mejoras para caballo:
* Se puede modelar como un camino hamiltoniano. Donde cada vertice es una casilla del tablero y las aristas entre ellos se dan segun como se moveria un caballo de estar en ese vertice.
```python
def problema_del_caballo():
  # debemos crear el grafo
  # por un lado, las 8x8 posiciones como vértices
  # luego se deben conectar con aristas los vértices, según movimiento del caballo
  camino = camino_hamiltoniano(grafo_construido_del_caballo)
  # reconstruir las posiciones del tablero según el camino
  # return solucion
```

```python
def caballo(paso = 0):
  if completo():  return True
  x, y = obtener_posicion_actual_caballo()
  for fila, col in movimientos_caballo(x,y):
    if not dentro_de_tablero(fila, col): continue
    if casillero_ya_marcado(fila, col): continue
    mover_a_posicion(fila, col, paso)
    if (caballo(paso + 1)): 
      return True
    volver_a_posicion(x,y)                                
  return False
```

```python
def camino_hamiltoniano_dfs(grafo, v, visitados, camino):
	visitados.add(v)
	camino.append(v)
	if len(visitados) == len(grafo):
		return True
	for w in grafo.adyacentes(v):
		if w not in visitados: # Esta es en sí nuestra poda
			if camino_hamiltoniano_dfs(grafo, w, visitados, camino):
				return True
	visitados.remove(v) 	# Permitiendo volver a venir a este vertice
	camino.pop()			# por otro camino
	return False

def camino_hamiltoniano(grafo):
camino = []
visitados = set()	
for v in grafo:	
		if camino_hamiltoniano_dfs(grafo, v, visitados, camino):
			return camino
	return None
```

```python
# MI SOLUCION ---> FALTA OPTIMIZAR
MOVIMIENTOS = (
        (-2, 1),
        (-2, -1),
        (-1, 2),
        (1, 2),
        (2, -1),
        (2, 1),
        (-1, -2),
        (1, -2),
    )


def es_posible(f,c, n, tablero):
    if 0 <= f < n and 0 <= c < n and tablero[f][c] == 0:
        return True
    return False

def caballo(n, fila,columna,casilla_actual, tablero):
    if casilla_actual == n**2:
        return True

    for y,x in MOVIMIENTOS:
        f, c = fila + y, columna + x  
        
        if es_posible(f, c, n, tablero):
            tablero[f][c] = casilla_actual
            if caballo(n, f, c, casilla_actual+1, tablero):    
                return True
            tablero[f][c] = 0
    return False

def completar_tablero(n):
    # for f in range(n):
        # for c in range(n):
    tablero = [[0]*n for _ in range(n)]
    tablero[0][0] = 1
    resultado = caballo(n, 0, 0, 2, tablero)
    if resultado:
        print(tablero)
    return resultado

completar_tablero(8)
```

### Dados
Escribir un algoritmo de tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya suma es s. Por ejemplo, con n = 2 y s = 7, debe devolver [1, 6] [2, 5] [3, 4] [4, 3] [5, 2] [6, 1].

¿De qué orden es el algoritmo en tiempo? ¿Y en memoria?

Mejoras en poda:
* Primero si S=8 y n=4.
	* Sacando [5, 2, ..., ...] me doy cuenta de que puedo podar porque me paso saque lo que saque en el dado 3 y 4.
* Idem para si no llego, ej: S=24 y n=5
	* Sacando [2, 3, ..., ..., ...] me doy cuenta que no llego a 24 no importa lo que saque.

```python
def suma_dados(suma, cant_faltan, solucion_parcial, soluciones):
    if sum(solucion_parcial) == suma and cant_faltan == 0:
        soluciones.append(list(solucion_parcial))
        return
	
    if sum(solucion_parcial) + cant_faltan*MIN_DADO > suma: return
    if sum(solucion_parcial) + cant_faltan*MAX_DADO < suma: return

    for valor in range(MIN_DADO, MAX_DADO+1):
        solucion_parcial.append(valor)
        suma_dados(suma, cant_faltan-1, solucion_parcial, soluciones)
        solucion_parcial.pop()
    return
```

Compljidad: $6^n$ para dados de 6 caras.

### Subset sum
Escribir una función que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva un subconjunto de L que sume exactamente n.

Por fuerza bruta tengo todo el algebra de probabilidades como los posibles subconjuntos que salgan. {vacio, todos los elementos, el primero solo, todos menos el primero, ...}


```
def obtenerCoordenadas():
  # metodo del objeto cuadrante que retorna los atributos y, x del mismo

def encontrarCuadranteDelSilo(cuadrante, silo):
  para cada cuadranteHijo de cuadrante:
    si cuadranteHijo contiene a silo:
      return cuadranteHijo # este contiene al silo

def encontrarYExcluirPiezaCentral(cuadrantePadre, cuadranteActual):
  si cuadranteActual tiene excluido:
    return
  y1, x1 = cuadrantePadre.obtenerCoordenadas()  
  y2, x2 = cuadranteActual.obtenerCoordenadas()
  direccion = 0  
  if x1 == x2:  
    if y1 == y2:  
	  # cuadranteActual esta en el 1er cuadrante de cuadrantePadre
      # por lo que el centro esta en la parte inferior derecha
      direccion = 3  
    elif y2 > y1:  
      # cuadranteActual esta en el 3er cuadrante de cuadrantePadre
      # por lo que el centro esta en la parte superior derecha
      direccion = 1  
  elif x2 > x1:  
    if y2 == y1:  
      # cuadranteActual esta en el 2do cuadrante de cuadrantePadre
      # por lo que el centro esta en la parte inferior izquierda       
      direccion = 2  
    elif y2 > y1:  
      # cuadranteActual esta en el 4to cuadrante de cuadrantePadre
      # por lo que el centro esta en la parte superior izquierda       
      direccion = 0

# creo variables auxiliares para iterar dentro de los cuadrantes, excluyendo en
# todos los hijos del cuadrante a excluir, hasta excluir la hectarea de 1x1 del
# cuadrante hijo mas chico que lo incluye

cuadranteAnt = cuadranteActual  
cuadranteAct = cuadranteActual.obtenerCuadrantes()[direccion]  
while cuadranteAct.obtenerDim() > 1:  
    cuadranteAnt.excluir(cuadranteAct)  
    cuadranteAnt = cuadranteAct  
    cuadranteAct = cuadranteAct.obtenerCuadrantes()[direccion]  
cuadranteAnt.excluir(cuadranteAct)

def seccionar(cuadrantePadre, cuadranteActual):
  si cuadranteActual incluye al silo:
    cuadranteAExcluir = encontraryExcluirCuadranteDelSilo(cuadranteActual, silo)
    cuadranteActual.excluir(cuadranteAExcluir)
  else:
    encontrarYExcluirPiezaCentral(cuadrantePadre, cuadranteActual)

  si el cuadranteActual es minimo (n=2):
    coloreo(cuadranteActual)
  else:
    para cada cuadranteHijo de cuadranteActual:  
      dibujar(cuadranteActual, cuadranteHijo)
```


"""
Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos.
El listado (ordenado por nombre del pueblo) contiene el número de kilómetros
donde está ubicada cada una. Se desea ubicar la menor cantidad de patrullas
policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con
vigilancia a más de 50 km. Proponer un algoritmo que lo resuelva.

Ejemplo (ciudad,Bifurcación):
(Castelli, 185), (Gral Guido, 249), (Lezama 156), (Maipu, 270), (Sevigne, 194).
Si incluimos un patrullero en la bifurcación de Lezama, cubre además de esta a Castelli y Sevigne.
Pero no Gral Guido y Maipú. Se necesitaría en ese caso, ubicar otro. Al agregar otro patrullero
en Gral Guido, se cubren todas las ciudades restantes. Con 2 móviles policiales en bifurcaciones
se cubren todas los accesos a todas las ciudades con distancia menor a 50km.

(Lezama 156), (Castelli, 185),  (Sevigne, 194), (Gral Guido, 249), (Maipu, 270).
156, 185, 194, 249, 270
"""
from math import inf
# lista = [(156, "Lezama"), (185, "Castelli"), (194, "Sevigne"), (249, "Gral Guido"), (270, "Maipu")]
# 130 195 225 230 270 280 330
lista = [130, 195, 225, 230, 270, 280, 330, inf]
# 130 195 225 230 270 280 330

# mientras no haya recorrido toda la lista
# agrega al anterior elemento del que este a mas de 50 km del minimo
# luego, busca el siguiente minimo considerando que es el mayor a 50 km del anterior agregado
# repite el proceso
i = 0
moviles = []
min = lista[i]
ant = i
n = len(lista)
while i < n:
    if lista[i] - min > 50:
        moviles.append(lista[ant])
        while i < n and lista[i] - lista[ant] <= 50:
            i += 1
        min = lista[i]
    ant = i
    i += 1

# 256

print(moviles)
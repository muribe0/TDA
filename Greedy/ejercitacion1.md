Realizar un seguimiento de aplicar el Algoritmo de Huffman al texto "PRETERINTENCIONALIDAD", indicando el binario
resultante de comprimirlo

16. El club de Amigos de Siempre prepara una cena en sus instalaciones en la que se desea invitar a la maxima cantidad
    de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un requisito: Solo puede ser invitada
    si conoce a al menos 4 personas invitadas.

    1. Nos solicitan seleccionar el mayor numero posible de invitados. Proponer una estrategia greedy optima para
       resolver el problema
    2. Los organizadores desean que cada invitado pueda conocer nuevas personas. Por lo que nos solicitan que
       adicionemos una nueva restriccion a la invitacion: Solo puede asistir si NO conoce al menos otras 4 personas
       invitadas. Modifique su propuesta para satisfacer esta nueva solucion.

12. Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad
    República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias
    locales no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos
    grupos por el control de diferentes kilómetros de la ruta costera.

    Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros (por ejemplo, la mafia nro 1 le pide del
    kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). Si hay una mafia tomando control de algún
    determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse). Cada mafia pide por un
    rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros
    pedidos. Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de
    interés es maximizar la cantidad de permisos otorgados (asegurándose de no otorgarle algún lugar a dos mafias
    diferentes). Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine
    a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando
    la cantidad de pedidos otorgados. Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué
    el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

Dado rangos en km (1 al 3.5 o 3.33 al 8, etc.) definir un algoritmo greedy que maximice la cantidad de rangos sin
superposicion. ESTO ES SCHEDULING! Ya resuelto

```python
def se_solapan(fin_1, inicio_2):
    return fin_1 > inicio_2


def asignar_mafias(pedidos):
    horarios = sorted(pedidos, key=lambda x: x[1])
    charlas = []
    fin_ant = 0
    for h in horarios:
        inicio, fin = h
        if not se_solapan(fin_ant, inicio):
            charlas.append(h)
            fin_ant = fin

    return charlas
```

## Bifurcaciones en Ruta

Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del
pueblo) contiene el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de policiales (en
las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.
Ejemplo:

| Ciudad     | Bifurcación |
|------------|-------------|
| Castelli   | 185         |
| Gral Guido | 242         |
| Lezama     | 156         |
| Maipú      | 270         |
| Sevigne    | 194         |

Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en
ese caso, poner otro. Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que
cubren todas los accesos a todas las ciudades con distancia menor a 50km.
En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única
solución óptima sería colocar un móvil policial en Sevigne.

#### Solucion
1. Ordenar por kilometro:

| Ciudad     | Bifurcación |
|------------|-------------|
| Lezama     | 156         |
| Castelli   | 185         |
| Sevigne    | 194         |
| Gral Guido | 242         |
| Maipú      | 270         |

2. Recorrer hasta encontrar una ciudad $i$ que no pueda cubrir a las anteriores descubiertas. Colocar un móvil en la
   ciudad anterior a $i$ y continuar. 

```python
def cubrir(ciudades):
    no_cubierto = ciudades[0]
    colocados = []
    for i in range(1, len(ciudades)):
        act = ciudades[i] # Ciudad actual es la i-ésima
        
        if colocados and colocados[-1] + 50 < act: # Si el anterior policia cubre la ciudad actual
            no_cubierto = act
            continue
            
        if act - no_cubierto > 50: # Si la primer ciudad no cubierta está a más de 50km
            # la cubro con un policia en la ciudad i-1
            colocados.append(ciudades[i-1])


```
def reconstruir_solucion(OPT, monedas):
    i, j = 0, len(monedas) - 1
    monedas_sophi = []
    """
    La reconstruccion de la solucion aprovecha la matriz S asociada que contiene todas las decisiones optimas de cada jugador para todos los subconjuntos [i,j] in [1, n].
    La matriz S, para cada valor i,j guarda la suma total de monedas elegidas por SOphia para el intervalo [i,j]. 
    Comenzamos el analisis, entonces, desde i=1,j=n debido a que S_1,n representa la sumatotal de monedas elegidas por SOhpia para el intervalo total de monedas (desde la primer a la ultima). Ese valor, entonces, representa la suma entre la ultima moneda elegida por Sophia y las otras que haya elegido. Sabemos que esta ultima moneda fue tomada teniendo en cuenta y aprovechando calculos previos que se encuentran dentro de la matriz. En particular, la decision de tomar la moneda 1 o la moneda n depende de la decision de Mateo para el intervalo restante. 
    
    La reconstruccion de la solucion, al igual que el algoritmo de construccion de la matriz S, considera la decision que tomaria Mateo:
    1. Se fija cuanto acumularía Sophia en caso de agarrar la primer moneda + S_i',j'
    2. Se fija cuanto acumularía Sophia en caso de agarrar la ultima moneda + S_i'',j''.
    3. Compara cual de los dos es mayor. El camino mayor entre 1 y 2 va a ser lo que eligió y el valor guardado en S_i,j
    4. Agrega entonces la primer o ultima moneda, segun la comparacion del paso 3 al conjunto de monedas elegidas por Sophia.
    5. Avanza i -> i+1 si es que 2>=3, Avanza j -> j-1 si es que 2<3
    6. Finalmente, sabiendo lo que ha decidido Mateo, se avanza un turno.
    """
    while i <= j:
        # Turno de Sophia
        if i == j:
            monedas_sophi.append(monedas[i])
            break

        # Si agarra la primera, me fijo que elije Mateo
        if monedas[i+1] > monedas[j]:
            i_izq, j_izq = i+2, j
        else:
            i_izq, j_izq = i+1, j-1

        if OPT[i][j] == monedas[i] + OPT[i_izq][j_izq]: # si Sohpia eligio la primera ...
            monedas_sophi.append(monedas[i])
            i, j = i_izq, j_izq
            continue

        if monedas[i] > monedas[j-1]:
            i_der, j_der = i+1, j-1
        else:
            i_der, j_der = i, j-2
        monedas_sophi.append(monedas[j])
        i, j = i_der, j_der

    return monedas_sophi

def juego(monedas):
    n = len(monedas)
    OPT = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(j, -1, -1):  # esto itera (f,c): (0,0)->(1,1)->(0,1)->(2,2)->(1,2)->(0,2)->...
            largo = abs(i - j) + 1

            if largo == 1:
                # Caso base
                OPT[i][j] = monedas[i]
            else:
                # Si toma la primer moneda, Mateo debe elegir la mejor de las que quedan:
                if monedas[i+1] > monedas[j]:
                    i_izq = i+2
                    j_izq = j
                else:
                    i_izq = i+1
                    j_izq = j-1

                # Si toma la ultima moneda, Mateo debe elegir la mejor de las que quedan:
                if monedas[i] > monedas[j-1]:
                    i_der = i+1
                    j_der = j-1
                else:
                    i_der = i
                    j_der = j-2

                OPT[i][j] = max(monedas[i] + OPT[i_izq][j_izq],  monedas[j] + OPT[i_der][j_der])


    return reconstruir_solucion(OPT, monedas)

def test20():
    ruta = "20.txt"
    with open(f"test-catedra/{ruta}", 'r') as archivo:
        resultado_esperado = 0
        for linea in archivo:
            if linea.startswith("$"):
                resultado_esperado = int(linea.strip()[1:])
                continue
            elif linea.startswith("#"):
                continue
            monedas = list(map(int,linea.strip().split(";")))

    if resultado_esperado > 0:
        resultado = juego(monedas)
        if sum(resultado) == resultado_esperado:
            print(ruta)
        else:
            print(sum(resultado), resultado_esperado, resultado)
            print(monedas)

def tests():
    rutas = ["5.txt", "10.txt", "20.txt", "25.txt", "50.txt", "100.txt", "1000.txt", "2000.txt", "5000.txt", "10000.txt"]
    # rutas = ["5.txt", "10.txt", "20.txt"]
    for ruta in rutas:
        with open(f"test-catedra/{ruta}", 'r') as archivo:
            resultado_esperado = 0
            for linea in archivo:
                if linea.startswith("$"):
                    resultado_esperado = int(linea.strip()[1:])
                    continue
                elif linea.startswith("#"):
                    continue
                monedas = list(map(int,linea.strip().split(";")))


        if resultado_esperado > 0:
            resultado = juego(monedas)
            print("Test", ruta)
            print("Resultado: ", resultado_esperado, "-"*30, "OK" if sum(resultado) == resultado_esperado else f"ERROR da {sum(resultado)}")
            print(resultado)




tests()
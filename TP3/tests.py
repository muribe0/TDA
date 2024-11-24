from verificador import verificador

def test(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    barcos = [int(x) for x in lineas[0].strip().split()]
    filas = [int(x) for x in lineas[1].strip().split()]
    columnas = [int(x) for x in lineas[2].strip().split()]
    S = []
    for linea in lineas[3:]:
        if linea[0] == "#" or linea[0] == "\n":
            continue
        fila = linea.strip().split()
        S.append([int(x) if x != "." else -1 for x in fila])
        print(fila)

    print(barcos)
    print(filas)
    print(columnas)

    assert verificador(S, filas, columnas, barcos) == True

test("test_0.txt")
test("10_10_10.txt")
from time import sleep
def imprimir_matriz(i, j, n, matriz):
    for l in range(n):
        for k in range(n):
            if i == l and j == k:
                matriz[i][j] = "X"
            print(matriz[l][k], end=" ")
        print()




def recorrido():
    n = 4
    matriz = [["_" for _ in range(n)] for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            print("*"*100)
            print(i, j)
            imprimir_matriz(i, j, n, matriz)
            sleep(1)

# recorrido()

def recorrido2():
    n = 4
    matriz = [["_" for _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(j, -1, -1):

            print("*"*100)
            print(i, j)
            imprimir_matriz(i, j, n, matriz)
            sleep(1)

recorrido2()
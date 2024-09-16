# Imports necesarios para el notebook
from random import seed

from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from random import randint
import time

# Siempre seteamos la seed de aleatoridad para que los # resultados sean reproducibles
seed(12345)
np.random.seed(12345)
sns.set_theme()

import sys
from collections import deque

def greedy(monedas):
    sofia, mateo = 0, 0
    turno_sophia = True

    while monedas:
        if turno_sophia:
            if monedas[0] > monedas[-1]:
                sofia += monedas.popleft()
            else:
                sofia += monedas.pop()
        else:
            if monedas[0] < monedas[-1]:
                mateo += monedas.popleft()
            else:
                mateo += monedas.pop()

        turno_sophia = not turno_sophia

    return sofia, mateo


def get_random_array(size: int):
    return np.random.randint(0, 100000, size)


# archivo = open("input.txt", "w")
# for n in contenido:
#     archivo.write(str(n) + "\n")

def pruebas(size):
    contenido = get_random_array(size)
    monedas = deque(map(int, contenido))
    inicio = time.time()
    s, m = greedy(monedas)
    fin = time.time()
    print(f"{s > m} - input: {size} tiempo: {fin-inicio}")
    return (size ,fin-inicio)

# F(X) = A x + B

resultados = []
for _ in range(30):
    n = randint(1000, 1000000)
    x, y = pruebas(n)
    resultados.append((x, y))

x = [point[0] for point in resultados]
y = [point[1] for point in resultados]

ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, y, "bo")
ax.set_ylim(0, 0.5)
ax.set_xlim(-0.1, 1000000)
plt.show()

ax: plt.Axes
fig, ax = plt.subplots()
ax.plot(x, [resultados[i] for i in x], label="Medición")
ax.set_title('Tiempo de ejecución de sorted')
ax.set_xlabel('Tamaño del array')
ax.set_ylabel('Tiempo de ejecución (s)')
plt.show()
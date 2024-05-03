def maxSubarray(v):
    maximoGlobal = v[0]
    maximoLocal = v[0]
    idxFinMaximo = 0

    n = len(v)
    for i in range(1, n):
        maximoLocal = max(maximoLocal, 0) + v[i]  # max(max(i-1), 0) + v[i]

        if maximoLocal > maximoGlobal:
            maximoGlobal = maximoLocal
            idxFinMaximo = i

    return maximoGlobal

v = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 4, -1, 2, 1
print(maxSubarray(v))
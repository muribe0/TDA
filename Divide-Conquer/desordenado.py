

def elemento_desordenado(arr):
    ant = arr[0]
    for e in arr:
        if e < ant:
            return ant
        ant = e

    return ant

arr = [1, 2, 3, 7, 5, 6, 8, 9, 10]
print(elemento_desordenado(arr))
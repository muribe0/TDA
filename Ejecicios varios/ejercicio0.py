class Alumno:
    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura

    def __repr__(self):
        return f'{self.altura}'

def indice_mas_bajo(alumnos):
    l = 0
    r = len(alumnos) - 1

    if alumnos[l].altura < alumnos[r].altura:
        return l
    elif alumnos[l].altura > alumnos[r].altura:
        return r

    while l < r:
        m = (l+r) // 2
        med, sig = alumnos[m].altura, alumnos[m+1].altura
        if med > sig: # si esta decreciendo, el menor esta a la derecha
            l = m + 1
        else:
            r = m

    return l

def validar_mas_bajo(alumnos, indice):
    return indice_mas_bajo(alumnos) == indice

def test():
    # alturas : 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.
    alumnos = [Alumno('a', 1.2), Alumno('b', 1.15), Alumno('c', 1.14), Alumno('d', 1.12), Alumno('e', 1.02), Alumno('f', 0.98), Alumno('g', 1.18), Alumno('h', 1.23)]

    print(validar_mas_bajo(alumnos, 5)) # 5

    alumnos = [Alumno('a', 1.2), Alumno('b', 1.15), Alumno('c', 1.14), Alumno('d', 1.12), Alumno('e', 1.02), Alumno('f', 0.98), Alumno('g', 1.18), Alumno('h', 1.23), Alumno('i', 1.24)]
    print(validar_mas_bajo(alumnos, 5)) # 5

    alumnos = [Alumno('a', 1.2), Alumno('b', 1.15), Alumno('c', 1.14), Alumno('d', 1.12), Alumno('e', 1.02), Alumno('f', 1.08), Alumno('g', 1.18), Alumno('h', 1.23), Alumno('i', 1.24), Alumno('j', 1.25)]
    print(validar_mas_bajo(alumnos, 4)) # 4

    alumnos = [Alumno('d', 1.12), Alumno('e', 1.02), Alumno('f', 1.08)]
    print(validar_mas_bajo(alumnos, 1)) # 1

    alumnos = [Alumno('d', 1.0), Alumno('e', 1.02), Alumno('f', 1.08), Alumno('g', 1.18)]
    print(validar_mas_bajo(alumnos, 0)) # 0

test()
import random
cartas = []

def generar_mazos(n):
    i = 1
    cartas = []
    for j in range(1, 4*n + 1,1):
        while i<= 13:
            cartas.append(i)
            i = i + 1
        i = 1
    return cartas

mazos1 = generar_mazos(2)

random.shuffle(mazos1)

def jugar(m):
    k = 0
    while k < 21:
        k = k + m.pop(0)
    return k


resultado = jugar(mazos1)
print(resultado)

def jugar_varios(m, j):
    generar_mazos(m)
    for l in range(1, j +1, 1):
        
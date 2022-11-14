def sumando(n):
    superLista = [[],[],[],[],[],[],[],[],[],[]]
    cubeta = 0
    inicio = 1
    fin = 10
    suma = 0
    while cubeta < 10:
        current = -1
        for k,i in enumerate(range(inicio,fin+1)):
            superLista[cubeta].append(i)
            suma+= i if k == n else 0
            current = i
        inicio = current + 1
        fin = inicio + 9
        print(superLista[cubeta])
        cubeta += 1
    return suma

n = int(input('Dame N: '))
print(sumando(n))
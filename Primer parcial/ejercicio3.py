"""
    Escribir una funcion llamada ordenaPositivos
    que dada una lista de numeros enteros (neg, pos)
    devuelva una nueva lista con los numeros positivos
    ordenados de mayor a menor y mantenga los numeros
    negativos en la misma posicion que la lista original
"""

def ordenaPositivos(numeros):
    numerosOrdenados = sorted([i for i in numeros if i > 0])
    for i in [(i,p) for i,p in enumerate(numeros) if p<0]:
        numerosOrdenados.insert(i[0], i[1])
    return numerosOrdenados
    
    
assert ordenaPositivos([6,3,-2]) == [3,6,-2]
assert ordenaPositivos([6,3,-2,5,-8,2,-2]) == [2,3,-2,5,-8,6,-2]

print('Pruebas pasadas')
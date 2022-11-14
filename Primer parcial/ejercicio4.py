"""
    Implementar una funcion llamada mapaCaracteres
    que recibe como argumento una palabra y devuelva
    un mapa de caracteres unico de una palabra
    El mapa de caracteres es una lista numerica en la
    que el numero 0 se corresponde con el primer caracter
    de la palabra, el 1 con el siguiente caracter y asi
    sucesivamente
"""

def mapaCaracteres(palabra):
    dictPalabras = {}
    contadorPosiciones = 0
    listaRetorno = []
    for letra in palabra:
        if letra not in dictPalabras:
            dictPalabras[letra] = contadorPosiciones
            contadorPosiciones+=1
        listaRetorno.append(dictPalabras[letra])
    return listaRetorno

assert mapaCaracteres('abcd') == [0,1,2,3]
assert mapaCaracteres('aabbcb') == [0,0,1,1,2,1]
assert mapaCaracteres('zagzdaa') == [0,1,2,0,3,1,1]

print('Pruebas pasadas')
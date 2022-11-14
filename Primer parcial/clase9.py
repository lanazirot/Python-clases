# Escribir un programa que reciba una cadena de caracteres y devuelva
# un diccionario con cada palabra que contiene y su frecuencia

# Escribir otra funcion que reciba el diccionario y devuelva una tupla
# con la palabra mas repetida y su frecuencia

def frecuenciaDiccionario(palabra: str):
    splitted = palabra.split(' ')
    diccionario = {}
    for palabra in splitted:
        if palabra in diccionario:
            diccionario[palabra] +=  1
        else:
            diccionario[palabra] = 1    
    return diccionario

def mayorFrecuencia(**dic):
    mayor = 0
    palabra = ''
    for k,v in dic.items():
        if v>mayor:
            mayor = v
            palabra = k            
    return (palabra,mayor)



cad = 'hola como estas estas como hola hola estas estas'
r1 = frecuenciaDiccionario(cad)
r2 = mayorFrecuencia(**r1)

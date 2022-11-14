"""
    Escribir un programa en el que se pregunte al usuario por una frase
    y una letra y mostrar en pantalla el numero de veces que se repite la
    letra
"""

frase = input('Ingresa la frase: ')
letra = input('Ahora ingresa la letra: ')
veces = 0
for char in frase:
    if char == letra:
        veces+=1
print(f'La letra se repite {veces} veces')
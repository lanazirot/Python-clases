"""
    Escribir un programa que guarde en un diccionario los precios
    de las frutas en la tabla, pregunte al usuario por una fruta,
    un numero de kilos, y muestre en pantalla el precio de ese 
    numero de kilos. Si la fruta no esta en el diccionario, debe 
    mostrar un mensaje acerca de ello
"""

frutas = {'Platano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

fruta = input('Fruta: ')
if fruta not in frutas:
    print('No existe la fruta en el diccionario')
else:
    kilos = float(input('Kilos: '))
    total = kilos * frutas[fruta]
    print("El total es de ${0:,.2f}".format(total))
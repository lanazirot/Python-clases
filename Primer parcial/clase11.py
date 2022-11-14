"""
    Escribir un programa que pregunte el nombre de un producto
    su precio y un numero de unidades y muestre por pantalla
    una cadena con el nombre del producto seguido de su precio unitario
    con 6 digitos digitos enteros y 2 decimales. El numero de unidades
    con 3 digitos y el coste total con 8 digitos enteros y 2 decimales
"""

nombre = input('Nombre del producto: ')
precio = float(input('Precio del producto: '))
numeroUnidades = int(input('Unidades: '))

cadena = "Nombre: {0}, con costo de ${1:,.2f} y el numero de unidades del producto es {2:,.3f} con coste total de ${3:0>8,.2f}".format(nombre,precio, numeroUnidades, (precio*numeroUnidades))
print(cadena)
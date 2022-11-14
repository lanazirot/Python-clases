# Tipos de datos

"""
    Una jugueteria tiene mucho exito en sus productos, payasos y muñecas
    Suele hacer su venta por correo y la empresa de logistica les cobra por
    peso de cada paquete. Deben calcular el peso de los payasos y muñecas
    que saldrán en cada paquete en demanda.
    
    Payaso = 112g
    Cada muñeca = 75g
    
    Escribir un programa que lea el numero de payasos y muñecas
    
    Calcule el peso total del paquete que sera enviado y el precio total del envio
    si por cada 100g de payaso se cobran 2.50$ y por cada 100g de muñeca 2$
"""


pesoPayaso = 112
pesoMuneca = 75

costoPayaso = 2.5
costoMuneca = 2

cantidadPayasos = int(input('Cantidad payasos'))
cantidadMunecas = int(input('Cantidad de munecas'))

pesoTotal = (cantidadPayasos * pesoPayaso) + (cantidadMunecas * pesoMuneca)
precioTotal = (((cantidadPayasos * pesoPayaso) * costoPayaso) / 100) + ((( cantidadMunecas * pesoMuneca) * costoMuneca) / 100)

print(f"El peso total es de {pesoTotal}g")
print("El total es de ${0:,.2f}".format(precioTotal))
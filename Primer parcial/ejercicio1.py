"""
    Implementar una funcion llamada ordenaCiudades
    que reciba como argumento un diccionario con
    ciudades y su poblacion y devolvera una lista
    de las ciudades de mas de 200mil habitantes
    La lista devuelva debe estar ordenada de mayor
    a menor
"""

def ordenaCiudades2(**ciudades):
    return [c[0] for c in sorted(ciudades.items(), key = lambda x: x[1], reverse=True) if c[1] > 200000]
    

ciudades = {
    'Madrid': 250000,
    'Juarez': 100000,
    'Laredo': 300000,
    'El Cairo': 6500000,
    'Peru': 60000,
    'Paris': 500000
}

print(ordenaCiudades2(**ciudades))
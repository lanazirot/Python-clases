"""
    Hacer un programa que reciba como entrada por teclado
    una secuencia de palabras separadas por espacios en 
    blanco, e imprima las palabras ordenadas alfanumericamente
    en mayusculas y despues de haber eliminado los duplicados
"""


print(sorted(set((input('Ingrese palabras separadas por espacios: ').upper().split(' ')))))

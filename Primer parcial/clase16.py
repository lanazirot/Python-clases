"""
    Modulos
"""
import clase16Operaciones as op
import csv
from clase16Operaciones import suma as s

with open('sample.csv') as f:
    r = csv.reader(f)
    for row in r:
        print(','.join(row))

"""
    Existen modulos que no vienen instalados en python
    Se usa pip xd
"""
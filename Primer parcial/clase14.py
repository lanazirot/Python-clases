"""
    Escribir un programa que almacene las matrices A y B
    Haga el producto entre ellos 2, y muestre el resultado en una lista
    Para almacenar las matrices utilice tuplas anidadas y para mostrar resultado
    use listas anidadas
"""

A = ((1,2,3), (4,5,6))
B = ((-1,0), (0,1), (1,1))
R =  [[],[]]



z = 0
for values in A:
    for i in range(len(A)):
        q=0; s=0
        for j in values:
            s+= j * B[q][i]
            q+=1
        R[z].append(s)
    z+=1

print(R)
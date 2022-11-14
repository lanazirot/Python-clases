x = 5
print("Es 5" if x==5 else "No es 5" )

a = 10
b = 0

lista = [[1,2,3,4], [4,'hola']]

for li in lista:
    for l in li:
        print(l)

for i in range(1, 10):
    print(i)

for i in "hola":
    if i == "l":
        continue
    else:
        print(i)

while x > 0:
    x-=1
    print(x)
else:
    print("Fin!")
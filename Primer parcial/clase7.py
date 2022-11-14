# Funciones :D
def function(x):
    print(f"Si le sabes {x}")

def otra(a,b,c):
    print(a+b+c)

otra(b=1, c=50, a=39)

listaNombres = ['Jesus', 'Maria', 'Alan']

def recorrerNombres(*nombres):
   for n in nombres:
       print(n)

recorrerNombres('Alan', 'Juan')

def suma(**numeros):
    suma = 0.0
    for k,v in numeros.items():
        suma+=v
    return suma

res = suma(hola=1, adios=2)
print(res)


d1 = {'clave': 10, 'segundaclave': 50}
res = suma(**d1)
print(res)

def sumaMedia(a,b,c):
    suma = a+b+c
    media = suma/3
    return suma,media

suma, media = sumaMedia(1,2,3)
print(suma,media)


def documentation():
    """
        Retorna 20
    """
    return 20

documentation()

help(documentation)
print(documentation.__doc__)

def documentado(a:str, b:int) -> str:
    """
        Retorna tu nombre y edad
    """
    return f"Hola {a} tienes {b} anios"

res = documentado('Hola', 20)
print(res)

def suma0A100():
    sumaX = 0
    for i in range(0,101):
        sumaX+=i
    return sumaX

sumaFinal = suma0A100()
print(sumaFinal)
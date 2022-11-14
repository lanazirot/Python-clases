#Expresiones lambda
# suma = (lambda a,b: print(a+b))
# suma(3,4)

# (lambda *n: print(sum(n)))(*list(range(0,101,1)))

# def multiplicado(n):
#     return lambda a: print(a*n)

# duplicador = multiplicado(2)

# duplicador(5)

#Input

# s = input('Hola ingesa tu nombre: ')
# print(s)

# #try catch

# try:
#     x = int(input('Ingresa un numero: '))
# except ValueError:
#     pass
# except TypeError:
#     pass
# except Exception as e:
#     print(e)
#     pass
# else:
#     print('jeje si paso...')
#     print(x)
# finally:
#     print('final...')

#assert

def suma(a,b):
    assert type(a) == int
    assert type(b) == int
    print(a,b)

suma(3,'d')




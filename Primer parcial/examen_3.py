"""
    EXTRA
"""
def fun(a,b):
    a = set(a)
    b = set(b)
    return [list(a&b),list(a^b)]
# Prueba
a = ['a', 'b', 2, 2, 3]
b = ['c','d',2, 'a', 4]
print(fun(a,b))


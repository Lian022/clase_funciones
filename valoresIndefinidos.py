def argumento (num):
    return type(num)

print(argumento(10))
print(argumento('cadena'))
print(argumento(20.11))

def argumento2 (*num):
    for i in num:
        print(i)
    return type(num)

print(argumento2(10))
print(argumento2('cadena'))
print(argumento2(20.11))
print(argumento2(10 , 20, 30, 40 ,50))
def nombre(name):
    
    return print('tu nombre es:', name.title())

name1= str(input("ingresa tu nombre: "))

nombre(name1)

#---------------------------------------------------------------------------------#

def tablasMultiplicar(numero):
    for i in range(1,11,1):
        print("{} x {} = {}".format(numero, i, i*numero))


numero = int(input("ingrese el numero que quiera multiplicar hasta 10: "))

tablasMultiplicar(numero)

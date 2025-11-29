#Escribir una función que reciba un número 
# entero positivo y devuelva su factorial.

def regresaFactorial(numero):
    if (numero<= 0):
        
        return print("el numero es negativo o 0, no se puede proceder")

    i = 1
    factorial = 1
    while i <= numero:
        factorial = factorial * i
        i = i + 1

    return print("El factorial de {} es {}".format(numero, factorial))

numero = int (input("ingresa tu numero: "))
regresaFactorial(numero)
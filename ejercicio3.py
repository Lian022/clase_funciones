#Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
# el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos 
# son iguales, debe retornar 0

def funcion():
    number1 = int(input('ingresa numero 1: '))
    number2 = int(input('ingresa numero 2: '))

    if (number1 > number2 ):
        return 1
    elif (number1 < number2 ):
        return -1
    else:
        return -1
    
print (funcion())
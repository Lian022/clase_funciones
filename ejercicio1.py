#Crear un programa que tenga una lista, luego crear una funcion con la cual se van 
# a pedir numeros al usuario para agregar a la lista. 
# Debes crear una segunda funcion en donde se ordenen los 
# numeros pares e impares dentro de dos listas nuevas

def llenarLista(cantidad):
    for i in range(cantidad):
        numero = int(input('ingrese el numero de la lista [{}]:'.format(i+1)))
        lista.append(numero)

    return lista 

def organizaLista(lista):
    pares = []
    impares = []

    for i in lista:
        if i%2 == 0:
            pares.append(i)
        else:
            impares.append(i)

    pares.sort()
    impares.sort()
    return print ('lista pares: ',pares, '\n','lista impares: ', impares)

lista = []
cantidad = int(input("ingrese la cantidad de numeros que quiera agregar a la lista: "))

llenarLista(cantidad)

print('lista normal: ',lista)

organizaLista(lista)


# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def muestra (lista):
    media = 0
    for i in lista:
        media = i/len(lista) + media

    return print(f"la media de la lista es : {media}")

lista = [10 , 20 , 30, 15 ,40]

muestra(lista)

#Escribir una función que reciba una muestra de numeros en una tupla y devuelva su medida.

def medida(*tupla):
    return print(tupla,len(tupla))



medida(15 , 30 , 30, 15 ,40)


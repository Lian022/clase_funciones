def entero():
    print('este es un dato entero: ')
    return 10

print(entero())

def decimal():
    print('este es un dato decimal: ')
    return 99

print(decimal())

def frase():
    print("esta es una frase: ")
    return "la frase es esta"

print(frase())

def asignacion():
    return 1, 2, 3, 4, 5, 6, 7


a, b, c, d, e, f, g = asignacion()

print(a, b, c, d, e, f, g)
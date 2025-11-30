#Crear un programa que tenga dos funciones, una que contenga el area de 
# un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio
import math

def areaCuadrado(base, altura):
    if (base != altura):
        return print("no es un cuadrado")
    
    area = base * altura

    return print (f"el area del cuadrado es: {area}")

def areaCirculo(radio):
    area = math.pi * pow(radio,2)

    return print (f"el area del circulo es: {area}")

areaCuadrado(10,10)
areaCirculo(10)

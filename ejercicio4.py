#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
# devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcular(cantidad, iva):
    if (iva !=0):
        if (iva >0):
            print('el total de la factura es: ',cantidad*(iva/100)+cantidad,'$' )
        else:
            print('el iva es negativo, no se puede proseguir')

    else: 
        print('el total de la factura es: ',cantidad*0.21+cantidad,'$' )


cantidad = float(input('ingrese la cantidad del producto: '))
iva = int(input('ingrese el porcentaje del iva: '))

calcular(cantidad, iva)


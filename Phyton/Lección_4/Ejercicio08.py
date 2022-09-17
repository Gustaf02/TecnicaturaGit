# Ejercicio 8: Menú interactivo. Cajero automático
# Hacer un programa que simule un cajero automático con un saldo
# inicial de 1000 $ y tendrá el siguiente número de opciones:
# Ingrese dinero en la cuenta
# Retirar dinero de la cuenta
# Mostrar dinero disponible
# Salir
saldo = 1000
while True:
    print('\t.Menú')
    print('1.Ingrese dinero en la cuenta')
    print('2.Retirar dinero de la cuenta')
    print('3.Mostrar dinero disponible')
    print('4.Salir')
    opcion = int(input('Digite una opción de menú'))
    print()
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar'))
        saldo += extra
        print(f'Dinero en la cuenta al momento ${saldo}')
    elif opcion == 2:
        retirar = float(input('Cuanto dinero desea retirar'))
        if retirar > saldo:
            print(f'no tiene esa cantidad de dinero {saldo}')
        else:
            saldo -= retirar
        print(f'Dinero en la cuenta al momento $ {saldo}')
    elif opcion == 3:
        print(f'Dinero en la cuenta al momento $ {saldo}')
    elif opcion == 4:
        print('Gracias por utilizar su cajero automático, hasta pronto')
        break
    else:
        print('Error, se equivocó de opción de menú')
        print()
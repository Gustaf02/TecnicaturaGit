# Ejercicio 5: Factorial de un número positivo
# Calcular el factorial de un número positivo
numero = int(input('Digite un número '))
while numero < 0:  # mientras el número sea positivo
    print('Error, el número tiene que ser positivo')
    numero = int(input('Digite un número '))
factorial = 1  # La variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial del número positivo  {numero} ingresado es {factorial}')


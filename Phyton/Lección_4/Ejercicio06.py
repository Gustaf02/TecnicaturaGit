# Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si digita el número 5 de la lista tendrá
# 5,10,15,20,25,30,35
numero = int(input('Ingrese un número por teclado'))
lista = []  # Creamos una lista vacía
for i in range(1, 11):
    lista.append(i*numero)
print(f'\nTabla de multiplicar {numero} : {lista}')

for indice, i in enumerate(lista):
    print(f'{numero} * {i} = {lista[indice]}')  # Este ciclo es para ver el formato de
# una tabla de multiplicar
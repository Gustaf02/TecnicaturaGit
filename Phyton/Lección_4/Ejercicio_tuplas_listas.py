import math  # importamos la clase math para hacer uso de la función sqrt (raíz cuadrada)
# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que sólo incluya los números menores a 5
# e imprima por consola [1, 3, 2]
lista = []  # Definimos la lista
# Filtramos los números menores a 5 de la lista
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de matemática
# Para sacar la raíz cuadrada de un número positivo
numero = int(input('Digite un número positivo'))
while numero < 0:
    print('Error, debería ser un número positivo')
    numero = int(input('Digite un número positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f} ')  # Antes importamos math como se ve arriba
# El .2f indica que se muestren sólo dos números
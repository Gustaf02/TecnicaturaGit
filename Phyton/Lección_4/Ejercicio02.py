# Modificar los elementos de una lista
# Llenar una lista con los números 1 al 10, luego modificar los elementos de la lista
# multiplicándolos por un valor ingresado por el usuario
lista = list(range(1, 11))
print('Lista original')
for i in lista:
    print(i, end='-')
valor = int(input('\nDigite un valor a multiplicar'))
# Multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):  # función para modificar los índices de la lista
    lista[indice] *= valor
print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')
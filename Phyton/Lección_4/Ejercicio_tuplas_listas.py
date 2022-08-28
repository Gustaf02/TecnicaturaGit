# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla
# Crear una lista que sólo incluya los números menores a 5
# e imprima por consola [1, 3, 2]
lista = []  # Definimos la lista
# Filtramos los números menos a 5 de la lista
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
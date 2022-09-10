# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas:
# en las que no debe haber repetición
# 1. listas de palabras que aparecen en las listas
# 2. listas de palabras que aparecen en la primera lista, pero no en la segunda
# 3. listas de palabras que aparecen en la segunda lista, pero no en la primera
# 4. listas de palabras que aparecen en ambas listas

# Creamos una lista
lista1 = [1, 2, 3, 'Gustavo', 'Ana', 'Ana', 4, 5, 2, 2, 4, 2, 1, 1]
lista2 = [1, 3, 'Natalia', 'Josefina', 'Natalia']

# Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2)  # unimos los dos conjuntos
solo1 = list(conjunto1 - conjunto2)  # solo muestra el conjunto 1
solo2 = list(conjunto2 - conjunto1)  # solo muestra el conjunto 2
interseccion = list(conjunto1 & conjunto2)  # mostramos ambas listas

print(union)
print(solo1)
print(solo2)
print(interseccion)
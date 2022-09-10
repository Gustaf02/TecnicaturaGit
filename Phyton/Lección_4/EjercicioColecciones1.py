# Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista y que, a continuación, elimine los elementos repetidos
# Por último, mostrar la lista

# Creamos una lista
lista = [1, 2, 3, "Gustavo", "Ana", "Ana", 4, 5, 2, 2, 4, 2, 1, 1]
# conjunto = set(lista)  # Se convierte lista a conjunto (set) ya que estos sólo admiten 1 vez
# lista = list(conjunto) # Se convierte el conjunto a lista
lista = list(set(lista))  # Conversión hecha en una línea de código de manera eficiente. Guardamos como # lo anterior
print(lista)
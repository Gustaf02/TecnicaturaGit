# Sintaxis de range(inicio (opcional), fin (requerido), incremento (opcional)

# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo 0,3,6,9
print("Rango de 0 a 10 con números divisibles por 2")
for i in range(11):
    # también for in range (0,11,1)
    if i % 3 == 0:
        print(i)

# Ejercicio 2: Crear un rango de números de 2 a 6 e imprímelos. Ej. 2,3,4,5,6
print("Rango de 2 a 6")
for i in range(2, 7, 1):
    print(i)

# Ejercicio 3: Crear un rango de números de 3 a 10 con un incremento de 2 en 2
# Ejemplo 3,5,7,9

print("Rango DE 3 A 10 con incremento de 2 en 2")
for i in range(3, 11, 2):
    print(i)
# Ejercicio 2: función con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numérico, utilizando argumentos variables *args como parámetros de la función y
# regresar como resultado de la multiplicación de todos los valores pasados como argumentos
def multiplicar_valores(*args):  # Es más utilizado argumentos en lugar de números
    resultado = 1  # El 0 no ayuda en la multiplicación
    for numero in args:
        resultado *= numero
    return resultado

# Llamamoa a la función


print(multiplicar_valores(3, 5, 15, 3))  # Le pasamos los argumentos
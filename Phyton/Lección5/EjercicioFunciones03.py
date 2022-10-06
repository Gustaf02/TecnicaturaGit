# Función recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivos
# Puede ser cualquier valor positivo. Si por ejemplo, usamos 5 imprimirá
# 5
# 4
# 3
# 2
# 1
# Si se ingresan números negativos no imprime nada
def imprimir_numeros_recursivos(numero):
    if numero >= 1:  # Caso base
        print(numero)
        imprimir_numeros_recursivos(numero - 1)  # Caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print('Valor ingresado incorrecto')


'''imprimir_numeros_recursivos(5)  # Esto si uno le ingresa el valor 5, por ejemplo'''
# Tarea, que el número lo ingrese el usuario

numerorecursivo = int(input('Digite el número para calcular el número recursivo: '))

imprimir_numeros_recursivos(numerorecursivo)
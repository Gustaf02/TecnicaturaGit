# Ejercicio 7: Juego adivina de un número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un número aleatorio entre 1 - 100, y luego ir pidiendo números indicando
# si es menor o mayor respecto a N.
# El juego termina cuando el usuario acierta y allí se debe mostrar el número de aciertos.
import random
aleatorio = random.randint(0, 100)  # Toma de 0 a 100 y se genera un número aleatorio
contador = 0
while True:
    numero = int(input('Digite un número'))
    contador += 1
    if numero > aleatorio:
        print('No es el número. Digite un número menor ')
    elif numero < aleatorio:
        print('No es el número. Digite un número mayor')
    else:
        print(f'FELICIDADES!!! Acabas de acertar el número{aleatorio}')
        break  # Rompe el ciclo y el bucle
    print('Numeros de intentos ', contador)
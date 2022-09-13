# Ejercicio 4 Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro de un rango. Por ejemplo: suma de números pares del
# 2 al 30. Suma = 240
a = int(input('Digite desde donde va a comenzar la suma '))
b = int(input('Digite hasta donde quiere que llegue a sumar '))
suma = 0
for i in range(a, b + 1):
    if i % 2 == 0:  # Esto es un número par
        suma += i
print(f'\nLa suma dentro de números pares es {suma}')

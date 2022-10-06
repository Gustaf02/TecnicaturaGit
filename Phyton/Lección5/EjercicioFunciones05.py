# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir grados celsius en farenheit y viceversa
# Investigar las fórmulas

# Función que convierte de celsius a farenheit
def celsius_farenheit(celsius):
    return celsius * 9 / 5 + 32  # la precedencia: multiplicación, división, suma

# Función que convierte de farenheit a celsius
def farenheit_celsius(farenheit):
    return (farenheit - 32) * 5 / 9  # Cambia la fórmula anterior. Se ponen paréntesis

celsius = float(input('Digite el valor de celsius '))
resultado = celsius_farenheit(celsius)
print(f'{celsius} C a F {resultado} : 2f')

farenheit = float(input('Digite el valor de farenheit '))
resultado = farenheit_celsius(farenheit)
print(f'{farenheit} F a C {resultado}: 2f')
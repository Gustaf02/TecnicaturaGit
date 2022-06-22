miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)
x=10
y=2
z=x+y
print(id(x))
#los literales se escriben x=960 y=704 z=024
print(id(y))
print(id(z))

#tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

#Manejo de cadenas (String)
miGrupoFavorito = "The Letter Black"
caracteristicas = "The Best Rock Band"
print("Mi grupo favorito es ", miGrupoFavorito, caracteristicas)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))

#tipos booleanos (bool)
miBoleano = 3 > 2
print(miBoleano)

if miBoleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

 #procesar la entrada del usuario
 #función input
 #resultado = input("Digite un número: ") #ingresa un dato tipo String
 #print(resultado)

#conversión de la entrada de datos
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f'El resultado de la suma es {suma}')

resta = operandoA - operandoB
print(f"El resultado de la resta es {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación es {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la división es {division}")
division = operandoA // operandoB
print(f"El resultado de la división es {division}")
modulo = operandoA % operandoB
print(f"El resultado de la división de módulo o residuo es {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es {exponente}")
""""""
...
""""""
alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))
area = alto*ancho
perimetro = (alto + ancho * 2)
print("Área: ", area)
print("Perímetro: ",perimetro)

miVariable3 = 10
print(miVariable3)
#Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -=2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *=3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3 /=2
print(miVariable3)

#Operadores de comparación
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

#Operador mayor que
resultado = d > b
print(resultado)

#Operador menor que
resultado = d < b
print(resultado)

#Operador menor o igual que
resultado = d <= b
print(resultado)

#Operador mayor o igual que
resultado = d >= b
print(resultado)

#Ejercicio Número par o impar
a = int(input("Digite un número: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
  print(f"El valor de a es: {a} es un número PAR")
else:
  print(f"El valor de a es:  {a} es un número IMPAR")

#Corroborar edad adulta
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >=edadAdulto:
  print(f"su edad es: {edadAdulto}: es mayor de edad")
else:
  print(f"Su edad es {edadPersona}: es menor de edad")

"""
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
print(f'El resultado de la suma es {suma}')

resta = operandoA - operandoB
print(f"El resultado de la resta es {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación es {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la división es {division}")
division = operandoA // operandoB
print(f"El resultado de la división es {division}")
modulo = operandoA % operandoB
print(f"El resultado de la división de módulo o residuo es {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es {exponente}")
""""""

""""""
alto = int(input("Proporciona el alto del rectángulo: "))
ancho = int(input("Proporciona el ancho del rectángulo: "))
area = alto*ancho
perimetro = (alto + ancho * 2)
print("Área: ", area)
print("Perímetro: ",perimetro)


miVariable3 = 10
print(miVariable3)
#Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -=2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *=3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3 /=2
print(miVariable3)

#Operadores de comparación
d = 4
b = 2
resultado = d == b #Comprobamos si son iguales
print(resultado)

#Operador diferente
resultado = d != b
print(resultado)

#Operador mayor que
resultado = d > b
print(resultado)

#Operador menor que
resultado = d < b
print(resultado)

#Operador menor o igual que
resultado = d <= b
print(resultado)

#Operador mayor o igual que
resultado = d >= b
print(resultado)


#Ejercicio Número par o impar
a = int(input("Digite un número: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
  print(f"El valor de a es: {a} es un número PAR")
else:
  print(f"El valor de a es:  {a} es un número IMPAR")

#Corroborar edad adulta
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >=edadAdulto:
  print(f"su edad es: {edadAdulto}: es mayor de edad")
else:
  print(f"Su edad es {edadPersona}: es menor de edad")

#Operadores lógicos

# operador and
a= True
b= False
resultado= a and b
print(resultado)

# operador or
resultado =45
a or b
print(resultado)

# operador not
resultado = not a
print(a)

# Ejercicio: valor dentro de un rango
valor = int(input("Digite un número dentro del rango 0  a 5 "))
valorMinimo= 0
valorMaximo= 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} está dentro del rango ")
else:
    print(f"El valor {valor} no está dentro del rango ")

# Ejercicio con el operador or y el operador not
vacaciones = False
diaDescanso = True
if not(vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("Tiene trabajo que hacer")

# Ejercicio: rango entre 20  y 30 años
edad = int(input("Digite su edad "))
#veinte = edad >= 20 and edad <30
#print(veinte)
#treinta = edad >= 30 and edad <40
#print (treinta)

#if veinte or treinta:
 #   print("Estás dentro del rango de los 20\' años ")
#elif treinta:
 #   print("Estás dentro del rango de los 30\' años")
#else:
 #   print("No estás dentro del rango de los 20\' a 30\' años")

# versión simplificada

# if(20 <= edad < 30 ) or (30 <= edad < 40):
 # print("Estás dentro del rango de los 20 a los 30")

# Ejercicio: el mayor de dos números
numero1 = int(input("Digite el valor del número 1 "))
numero2= int(input("Digite el valor del número 2"))

if numero1 > numero2:
    print("el número 1 es mayor")
else:
    print("El número 2 es mayor")

#Ejercicio Tienda de libros
print("Digite los siguientes datos del libro ")
nombre = input("Digite el nombre del libro")
id = int(input("Digite el ID del libro "))
precio = float(input("Digite el precio del libro"))
envioGratuito = input("Indicar si el libro es gratuito (True/False): ")
if envioGratuito == "True":
    envioGratuito = True
elif envioGratuito == "False":
    envioGratuito = False
else:
    envioGratuito = "El valor es incorrecto, debe escribir True o False"
print(f'''
        Nombre: {nombre}
        Id: {id}
        Precio: {precio}
        Envío Gratuito: {envioGratuito}
''')

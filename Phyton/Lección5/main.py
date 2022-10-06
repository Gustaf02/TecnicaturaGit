# Comenzamos con funciones
# Antes de llamarla hay que definirla
# Definimos una función
def mi_funcion():  # Para indentificar a una función utilizamos paréntesis
    print('Saludos a todos los alumnos de la tecnicatura')


mi_funcion()  # Estamos llamando a la función
mi_funcion()  # Se puede llamar a la función una N cantidad de veces
mi_funcion()


# Desempaquetado de lista o list despacking
def show(name, lastname):
    print(name + ' ' + lastname)


person = ['Gustavo', 'Ortiz']
show(person[0], person[1])  # Pasamos 1 a 1 los datos de la lista a la función
show(*person)  # Esto es lo mismo que lo anterior, pero le pasamos todo.
person2 = ('Ariel', 'Betancud')  # Desempaquetamos a través de una tupla
show(*person2)
person3 = {'lastname': 'Lucero', 'name': 'Natalia'}  # Diccionario
show(**person3)  # Se coloca ** porque se utilza clave y valor

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break  # Esta es la única manera para que el else no se ejecute. Aparte muestra hasta el 3
else:
    print('Esto se terminó')

# list comprehesion, lista de comprensión
names = ['Pepe', 'Rodrigo', 'Lupe', 'Amalia', 'Paolo']
alongP = [p for p in names if p[0] == 'P']  # Esto regresa una nueva lista
print(alongP)

bottleC = [{'name': 'Quilmes', 'country': 'Arg'},
           {'name': ' Corona', 'country': 'México'},
           {'name': 'Stella Artois', 'country': 'Belgium'},
           ]
Arg = [b for b in bottleC if b['country'] == 'Arg']
print(Arg)
print(bottleC)


# Paso de argumentos (funciones)
def mi_funcion2(name, lastname):
    print('Saludos a todos los que miran a traves del canal de youtube')
    print(f'nombre: {name}, apellido {lastname}')


mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')


# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b


# resultado = (78, 22)
# print(f'El resultado de la suma es {resultado}')
print(f'El resultado de la suma es {sumar(22, 34)}')


# Resultado por default
def sumar2(a=0, b=0):  # Le damos un valor por default
    return a + b


resultado = sumar2()
print(f'Resultado de la suma {resultado}')
print(f'Resultado de la suma {sumar(4, 6)}')


# Argumentos, variables en funciones
def listarnombres(*nombres):  # Cuando desconocemos el número de argumentos ponemos *
    for nombre in nombres:  # Se convierte en tupla
        print(nombre)


listarnombres('José', 'Daniel', 'Jorge', 'Leo', 'Amalia')
listarnombres('Marcos', 'Romina', 'Teresa')


def listarterminos(**terminos):  # lo más utilizado es **kwargs para recibir los argumentos

    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")


listarterminos()  # no recibe nada, nada se mostrará
listarterminos(IDE='Integrated Development Environment', PK='pRI')


def desplegarnombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres2 = ('Tito', 'Pedro', 'Carlos')
desplegarnombres(nombres2)
desplegarnombres('Carla')
desplegarnombres((10, 11))  # el () es de tupla. Para recorrer números hay que convertirlos a tupla
# si colocamos un sólo elemento no olvidar la coma. Por ejemplo (( 10,))
desplegarnombres([12, 14])  # la convertimos a lista para que recorra los números


# Funciones recursivas
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)  # Caso recursivo


numerofactorial = int(input('Digite el número para calcular el factorial: '))

resultado = factorial(numerofactorial)  # Lo hacemos con código duro
print(f'El factorial del número {numerofactorial} es {resultado}')

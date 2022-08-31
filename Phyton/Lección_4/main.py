# lista = Ariel, Natalia, Liliana, Osvaldo
# Colecciones en Python
# Las listas se conocen en otros lenguajes como arreglos o vectores

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2])
# sólo muestra el índice 0 y 1, pero no muestra el 2
# Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
# índice a mostrar: 0,1,2
# Desde el índice indicado hasta el final
print(nombres[1:])
# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# iterar una lista
for nombre in nombres:
    # nombre es singular, es el nombre de la variable. La lista es plural
    print(nombre)
else:
    print('se acabaron los elementos de la lista')

# preguntamos cuántos elementos tiene una lista
print(len(nombres))
# le pasamos como parámetro la lista

# Agregamos un elementos
nombres.append('Marcelo')
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])  # Agrego otra lista
nombres.append(7)
print(nombres)

# Insertar un nuevo elemento en un índice específico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Débora')
print(nombres)

# Eliminamos un elemento de la lista
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

# Eliminar un índice específico
del nombres[2]
# del significa delete (eliminar)
print(nombres)

# Eliminar, limpiar o borrar todos los elementos de la lista
nombres.clear()
print(nombres)
'''
# Elimina la lista
del nombres
print(nombres) #Aparece como error ya que la lista ha sido eliminada'''

# Definiendo una tupla.
cocina = ('cuchara', 'cuchillo', 'tenedor')
# Vemos la cantidad de elementos
print(len(cocina))

# Para acceder a un elemento
print(cocina[0])

# Mostrar de manera inversa
print(cocina[-1])

# Acceder a un rango
print(cocina[0:2])

# Ejemplo: es tupla necesita una coma, aunque sea de un elemento
tupla = ('papa',)
# De lo contrario sólo sería un tipo String, cadena

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar)
# print usa la diagonal inversa\ para el salto de línea. Aparece cada elemento debajo del otro
# Si quiero que los elementos aparezcan en una misma línea lo hago de esta manera
# print(cocinar, end=' ') Usamos end para eliminar los saltos de línea

# Hago una conversión de tupla a lista, y viceversa si quiero modificar un elemento, ya que la tupla es inmutable
# No es buena práctica hacer esto
cocinaLista = list(cocina)
cocinaLista[0] = 'plato'
cocina = tuple(cocinaLista)
print('\n', cocina)
# Agrego el salto de línea para que vea en una línea
'''
# Para eliminar una tupla
del cocina
print(cocina)'''

# Tipo set
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)  # cada vez que ejecutamos va cambiando el orden. Esa es una característica del set
# Si coloco print(len(planetas)) me mostrará el largo. length(len) es largo. Aparecerá un 3

# Revisar si un elemento existe dentro de un set
print('Marte' in planetas)  # Aparece un True. Si ponemos print('Marte' not in planeta) aparece False

# Agregar un elemento
planetas.add('Tierra')  # add es una función
print(planetas)

# Eliminar elementos. Puede arrojar un error si el elemento no existe
planetas.remove('Júpiter')
print(planetas)

# 'Maradona':10 Un diccionario está compuesto por dos elementos
# Una llave y un valor
# dict(key, value)
diccionario = {'IDE': 'Integrated Development Environment',
               'POO': 'Programación Orientada a objetos',
               'SABD': 'Sistema de Administración de Base de Datos'}
# Verificar la cantidad de elementos de un diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un elemento con la llave (key)
print(diccionario['IDE'])
# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Cómo recorrer un diccionario
for termino in diccionario:  # Recorremos solo las llaves
    print(termino)

# Necesitamos una función para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor)

# Otra manera de acceder a un diccionario
for termino in diccionario.keys():  # Estamos usando una función
    print(termino)  # Muestra solo las llaves

# Usamos una función para acceder al valor
for valor in diccionario.values():
    print(valor)  # Muestra valor sin llaves

# Comprobar la existencia de algún elemento
print('IDE' in diccionario)  # Devuelve un booleano. Si quiero que sea False pongo not in

# Agregar un elemento
diccionario['Pk'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario  # El diccionario se borra

# Concatenar listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9])  # Agregar varios elementos a la lista
print(lista3)

# Función para saber en qué índice está un valor ingresado
print(lista3.index(5))

# print(lista3.index(8)) Esto daría error porque el valor 8 no está en la lista

# Cómo saber cuántos valor repetidos hay en una lista
print(lista3.count(1))  # Cuenta cuántos valores 1 hay dentro de una lista

# Colocar nuestra lista al revés
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Método de ordenamiento, función en python
lista3.sort()  # Ordena los elementos ascendentemente por default
print(lista3)
lista3.sort(reverse=True)  # Ordena de manera descendente
print(lista3)

# Repaso de tuplas. Puede tener distintos tipos de elementos
tupla = (4, 'Hola', 6.78, [1, 2, 78], 4, 'Hola')
print(tupla)

print(4 in tupla)  # Respuesta booleana. Respuesta de tipo booleana
# Lo que podemos usar dentro de la tupla es index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto / para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)  # Preguntamos si el número 3 no está en el conjunto 1

# Como establecer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano

# Operaciones con conjuntos
conjunto3 = conjunto1 | conjunto2  # La línea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # Muestra qué elementos tienen en común
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # Qué valor está en conjunto 1 y no en el 2
print(conjunto3)

conjunto3 = conjunto2 & conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)  # Elementos que no comparten o que son diferentes entre ambos

conjunto3 = conjunto1 | conjunto2
print(conjunto3.issuperset(conjunto3))  # Aquí preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issuperset(conjunto3))
print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# Como saber si dos conjuntos son inconexos, es decir si no comparten elementos en común
print(conjunto1.isdisjoint(conjunto2))  # No hay cosas en común

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # Esto hace que el conjunto sea inmutable
# No se pueden agregar, modificar ni eliminar elementos del conjunto

# Repaso diccionarios
diccionarioNuevo = {'Azul': 'blue', 'Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel': {'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extr. Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Def. Ctral'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
}

# Agregar elementos al diccionario.
AgregoJugadores = {
    7: {'Nombre': 'Rodrigo De Paul', 'Edad': 28, 'Altura': 1.8, 'Precio': '20 millones', 'Posicion': 'Centrocampista'},
    22: {'Nombre': 'Lautaro Martínez', 'Edad': 25, 'Altura': 1.8, 'Precio': '10 millones', 'Posicion': 'Delantero'},
    8: {'Nombre': 'Leandro Paredes', 'Edad': 28, 'Altura': 1.8, 'Precio': '15 millones', 'Posicion': 'Centrocampista'},
    }

seleccionArgentina.update(AgregoJugadores)  # Se agregan, en primer lugar, tres elementos al diccionario

# A continuación, se agregan dos elementos más al diccionario quedando un total de 10 jugadores
seleccionArgentina[2] = {'Nombre': 'Lucas Martínez', 'Edad': 26, 'Alt': 1.81, 'Precio': '9.6 millones', 'Pos.': 'Def.'}
seleccionArgentina[6] = {'Nombre': 'Germán Pezzella', 'Edad': 31, 'Alt': 1.87, 'Precio': '8.5 millones', 'Pos.': 'Def.'}

for llave, valor in seleccionArgentina.items():  # Utilizamos una función para recorrer el diccionario
    print(llave, valor)

print('tenemos cargados en el diccionario la cantidad de: ', end=" ")
print(len(seleccionArgentina))  # Con len vemos la cantidad de jugadores

# Pilas usando listas
pila = [1, 2, 3]
'''
# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)'''

# Sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quita el último elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora queda de esta manera: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo (first imput/ first oupput): primero en llegar primero en salir
# Ejemplo: cola del banco

cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
'''
# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('José')
print(cola)'''

# Sacamos elementos de la lista
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)
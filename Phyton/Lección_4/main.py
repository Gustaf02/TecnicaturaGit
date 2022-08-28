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
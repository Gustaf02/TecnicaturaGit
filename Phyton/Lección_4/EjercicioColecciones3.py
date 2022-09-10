# Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# nombre: Aragorn
# clase: Guerrero
# Raza: Dunadan del norte

# nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legoles
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []  # Creamos una lista vacía
# Creamos diccionarios
P = {'Nombre': 'Aragorn', 'Clase': 'guerrero', 'Raza': 'Dunadan del Norte'}
personajes.append(P)  # Agregamos a la lista otro personaje
P = {'Nombre': 'Gandalf', 'Clase': 'mago', 'Raza': 'istar'}
personajes.append(P)  # Agregamos a la lista otro personaje
P = {'Nombre': 'Legolas', 'Clase': 'arquero', 'Raza': 'elfo sindar'}
personajes.append(P)
# Ejercicio: agregar otros tres personajes
P = {'Nombre': 'Frodo', 'Clase': 'portador del anillo', 'Raza': 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Gimli', 'Clase': 'compañía del anillo', 'Raza': 'enano'}
personajes.append(P)
P = {'Nombre': 'Arwen', 'Clase': 'reina', 'Raza': 'peredhil'}
personajes.append(P)
print(personajes)
# Ejercicio 11:
# Agenda telefónica:
# Hacer un programa que simule una agenda de contacto. Crear un diccionario donde la clave sea el
# nombre del usuario y la clave sea el teléfono. El programa tendrá el siguiente menú de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir
agenda = {}
while True:
    print('\nMenú: ')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción de Menú '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto ')
        telefono = input('Digite el número de teléfono ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('Este nombre de contacto ya existe')

    elif opcion == 2:
        nombre = input('¿Cuál es el nombre del contacto? ')
        telefono = input('Digite el número de teléfono ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contacto')
        for clave, valor in agenda.items():
            print(f'Nombre {clave}, Teléfono{valor}')
    elif opcion == 4:
        print('Gracias por ingresar su agenda de contactos')
        break
    else:
        print('Se equivocó de opción de menú')
    print()

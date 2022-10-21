from Persona2 import Persona2  # Si se pone asterisco, en lugar de Persona2 importa todo

print('Creación de objetos'.center(50, '-'))
if __name__ == 'main':
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalles()

    print(__name__)  # Permite una comprobación

print('Eliminación de objetos'.center(30, '-'))

#  del persona5
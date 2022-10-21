class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Método Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método setter. Se necesita un parámetro más que en el getter
        print('Estamos utilizando el método set')
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Método Getter
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método setter
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Método Getter
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método setter
        self._edad = edad


#  def __del__(self):                  no es muy común
#  print(f'Persona 2 {self._nombre} {self._apellido} {self._edad}')

if __name__ == 'main':  # puedo marcar el código que sigue y con tab se puede identar

    persona1 = Persona2('Ariel', 'Betancud', 41)

    print(persona1.nombre)  # Llamamos al método getter

    persona1.nombre = 'Juan Pedro'  # Llamamos al método setter
    print(persona1.nombre)  # Otra vez con el método getter
    persona1.mostrar_detalles()  # Llamamos al método mostrar_detalles
    print(persona1.edad)  # Atributo read only (sólo lectura)- Sería la edad porque no tiene el método set

    #  Tarea: crear tres objetos más utilizando los métodos getters y setters
    #  para modificar y mostrar y los cambios con el método mostrar detalles

    persona2 = Persona2('Gustavo', 'Ortiz', 43)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Gustavo'
    persona2.apellido = 'Ortiz'
    persona2.edad = 40
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Diana', 'Genín', 60)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Diana'
    persona3.apellido = 'Genín'
    persona3.edad = 20
    print(persona3.mostrar_detalles())

    persona4 = Persona2('Gabriela', 'Robles', 50)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Gabriela'
    persona4.apellido = 'Robles'
    persona4.edad = 45
    print(persona4.mostrar_detalles())

    print(__name__)  # Esto permite comprobar dónde se ejecuta el código

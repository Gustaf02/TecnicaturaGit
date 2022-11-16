# Alumno: Carlos Gustavo Ortiz

class Persona:
    contador_personas = 0  # Variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1  # se va incrementando de uno en uno
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()  # cada objeto que se crea recibe un id diferente
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  # método str
        return f'Persona [{self.id_persona} = {self.nombre} {self.edad}]'


persona1 = Persona('Gustavo', 40)  # Se comienza con la instancia
print(persona1)
persona2 = Persona('Diego', 70)
print(persona2)
persona3 = Persona('Gonzalo', 37)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona('Natalia', 35)
print(persona4)

print(f'Valor contador personas: {Persona.contador_personas}')

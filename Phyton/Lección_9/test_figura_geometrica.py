from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación de objeto clase cuadrado'.center(50,'_'))

cuadrado1 = Cuadrado(5, 'Azul')
cuadrado1.alto = -10
#  print(cuadrado1.ancho)
#  print(cuadrado1.alto)
print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')

# MRO = Method Resolution Order
print(Cuadrado.mro())

print(cuadrado1)
print('Creación de objeto clase rectángulo'.center(50,'_'))
rectangulo1 = Rectangulo(3, 8, 'verde')
rectangulo1.ancho = 15

print(f'Cálculo del área del rectángulo  {rectangulo1.calcular_area()}')
print(rectangulo1)

# figura1 = FiguraGeometrica()   # Pide importar  No se puede instanciar. Es abstracta.

print(Cuadrado.mro())
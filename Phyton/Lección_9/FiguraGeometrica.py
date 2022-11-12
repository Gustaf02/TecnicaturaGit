from abc import ABC, abstractmethod


# ABC significa: Abstract Base Class, convierte una clase en abstracta
class FiguraGeometrica(ABC):  # eS hija de ABC
    def __init__(self, ancho, alto):

        if self._validar_valores(ancho):
            self._ancho = ancho  # _ancho se encapsula, usamos entonces get y set
        else:
            self._ancho = 0
            print(f'El valor es erróneo para el ancho {ancho}')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._ancho = 0
            print(f'El valor es erróneo para el alto {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f'dato erroneo para el ancho{ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'dato erroneo para el alto{alto}')

    @abstractmethod  # hace que en cuadrado, rectángulo sea obligatorio que esté el método
    def calcular_area(self):
        pass

    def __str__(self):
        return f'Figura geométrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _validar_valores(self, valor):  # Método encapsulado
        return True if 0 < valor < 10 else False

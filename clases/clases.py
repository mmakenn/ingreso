from math import pi

class Circulo:
    def __init__(self, radius):
        if (radius <= 0):
            raise ValueError('El radio debe ser mayor a cero.')
        self._radius = radius

    def __str__(self):
        return "Circulo radio: " + str(self._radius)

    def __mul__(self, n):
        if (n <= 0):
            raise ValueError('No se puede multiplicar por un número menor o igual a cero.')
        return Circulo(self._radius * n)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, newRadius):
        if (newRadius <= 0):
            raise ValueError('El radio debe ser mayor a cero.')
        self._radius = newRadius

    def area(self):
        return pi*self._radius**2

    def perimeter(self):
        return 2*pi*self._radius

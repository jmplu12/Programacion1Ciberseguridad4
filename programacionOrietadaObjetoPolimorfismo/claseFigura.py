#3. Crea una clase base **Figura** con un método area(). Implementa clases hijas como Círculo y Cuadrado que calculen el área según corresponda.
import math
class Figura:
    def area(self):
        pass
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
# Ejemplo de uso:
circulo = Circulo(5)
cuadrado = Cuadrado(4)  
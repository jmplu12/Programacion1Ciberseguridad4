#Crea una clase llamada **Rectangulo** que reciba base y altura. 
# mplementa una función que calcule el área.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
# Ejemplo de uso
rectangulo = Rectangulo(5, 10)
print("El área del rectángulo es:", rectangulo.area())  # Salida: El área del rectángulo es: 50


# Clase interactiva que pide datos por teclado
class Rectagundo:
    """Clase `Rectagundo` que permite leer base y altura desde teclado
    y calcular área y perímetro."""
    def __init__(self, base: float = 0.0, altura: float = 0.0):
        self.base = base
        self.altura = altura

    def leer_desde_teclado(self) -> None:
        """Solicita base y altura al usuario por teclado y las guarda como floats.
        Reintenta si la entrada no es numérica."""
        while True:
            try:
                b = input("Ingrese la base del rectángulo: ").strip()
                a = input("Ingrese la altura del rectángulo: ").strip()
                self.base = float(b)
                self.altura = float(a)
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese números (ej: 3.5). Intentelo de nuevo.")

    def area(self) -> float:
        return self.base * self.altura

    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)


if __name__ == '__main__':
    print("Demo interactiva de la clase Rectagundo")
    r = Rectagundo()
    r.leer_desde_teclado()
    print(f"Base: {r.base} - Altura: {r.altura}")
    print(f"Área: {r.area()}")
    print(f"Perímetro: {r.perimetro()}")

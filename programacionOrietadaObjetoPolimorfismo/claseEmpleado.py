#2. Crea una clase base **Empleado** con atributos nombre y salario. Crea clases hijas como Gerente y Técnico, cada una con un método calcular_bono() diferente.
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")
class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20  # El bono del gerente es el 20% del salario
class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10  # El bono del técnico es el 10% del salario
# Ejemplo de uso:
gerente = Gerente("Ana", 5000)
tecnico = Tecnico("Luis", 3000) 
print(f"Bono del gerente {gerente.nombre}: {gerente.calcular_bono()}")
print(f"Bono del técnico {tecnico.nombre}: {tecnico.calcular_bono()}")  
# Salida:
# Bono del gerente Ana: 1000.0
# Bono del técnico Luis: 300.0  

#3. Crea una clase llamada **Coche** con atributos marca y velocidad. 
# Agrega una función que aumente la velocidad.

class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        return self.velocidad   
# Ejemplo de uso
coche = Coche("Toyota")
print("Velocidad inicial del coche:", coche.velocidad)  # Salida: Velocidad inicial del coche: 0
coche.acelerar(20)
print("Velocidad después de acelerar:", coche.velocidad)  # Salida: Velocidad después de acelerar: 20
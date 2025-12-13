#1. Crea una clase llamada **Usuario** con atributos nombre y edad. 
# Implementa una función que muestre los datos del usuario.
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
# Ejemplo de uso
usuario1 = Usuario("Juan", 30)  
print(usuario1.mostrar_datos())  # Salida: Nombre: Juan, Edad: 30
usuario2 = Usuario("Ana", 25)  
print(usuario2.mostrar_datos())  # Salida: Nombre: Ana, Edad: 25

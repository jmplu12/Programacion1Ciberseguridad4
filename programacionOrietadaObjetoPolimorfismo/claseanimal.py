#1. Crea una clase base llamada **Animal** con un método hablar(). 
# Luego crea clases hijas como Perro y Gato que sobreescriban el método.
class Animal:
    def hablar(self):
        raise NotImplementedError("Subclasses must implement this method")  
class Perro(Animal):
    def hablar(self):
        return "Guau"
class Gato(Animal):
    def hablar(self):
        return "Miau"
# Ejemplo de uso
if __name__ == "__main__":
    animales = [Perro(), Gato()]
    for animal in animales:
        print(animal.hablar())





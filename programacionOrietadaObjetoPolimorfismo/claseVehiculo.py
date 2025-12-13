#4. Crea una clase **Vehiculo** con un método mover(). Crea clases hijas como Carro y Bicicleta que implementen su propia versión del método.
class Vehiculo:
    def mover(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas.")    
class Carro(Vehiculo):
    def mover(self):
        return "El carro se está moviendo sobre ruedas."    
class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta se está moviendo pedaleando."
# Ejemplo de uso
carro = Carro()
bicicleta = Bicicleta() 
print(carro.mover())        # Salida: El carro se está moviendo sobre ruedas.
print(bicicleta.mover())    # Salida: La bicicleta se está moviendo pedaleando.

        
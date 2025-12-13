#5. Crea una clase **Dispositivo** con un método encender(). Crea clases hijas como Laptop y Teléfono que sobreescriban el comportamiento del método.
class Dispositivo:
    def encender(self):
        return "El dispositivo se está encendiendo."
class Laptop(Dispositivo):
    def encender(self):
        return "La laptop se está encendiendo con el botón de encendido."
class Telefono(Dispositivo):
    def encender(self):
        return "El teléfono se está encendiendo con el botón lateral."
# Ejemplo de uso
dispositivo = Dispositivo()
laptop = Laptop()
telefono = Telefono()
print(dispositivo.encender())  # Salida: El dispositivo se está encendiendo.
print(laptop.encender())       # Salida: La laptop se está encendiendo con
print(telefono.encender())     # Salida: El teléfono se está encendiendo con el botón lateral. el botón de encendido.
        
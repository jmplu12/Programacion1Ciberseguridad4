#5. Crea una clase llamada **Estudiante** con nombre y calificaciones. 
# Implementa una función que calcule el promedio.
class Estudiante:
    def __init__(self, nombre: str, calificaciones: list[float] = None):
        self.nombre = nombre
        self.calificaciones = calificaciones if calificaciones is not None else []

    def agregar_calificacion(self, calificacion: float) -> None:
        """Agrega una calificación a la lista de calificaciones del estudiante."""
        self.calificaciones.append(calificacion)

    def promedio(self) -> float:
        """Calcula y devuelve el promedio de las calificaciones del estudiante."""
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def solicitar_desde_teclado(self) -> None:
        """Solicita el nombre y las calificaciones por teclado.
        Para las calificaciones, el usuario puede ingresar una por línea y
        terminar con 'fin' o dejando la línea vacía."""
        # Nombre
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            self.nombre = nombre

        # Calificaciones
        print("Ingrese calificaciones una por una. Escriba 'fin' o deje vacío para terminar.")
        while True:
            entrada = input("Calificación: ").strip()
            if entrada == '' or entrada.lower() == 'fin':
                break
            try:
                cal = float(entrada)
                self.agregar_calificacion(cal)
            except ValueError:
                print("Entrada inválida. Ingrese un número (ej: 8.5) o 'fin' para terminar.")


if __name__ == '__main__':
    print('Demo interactiva de Estudiante')
    est = Estudiante('', [])
    est.solicitar_desde_teclado()
    print(f"Nombre: {est.nombre}")
    if est.calificaciones:
        print(f"Calificaciones: {est.calificaciones}")
        print(f"Promedio: {est.promedio()}")
    else:
        print("No ingresó calificaciones.")
    
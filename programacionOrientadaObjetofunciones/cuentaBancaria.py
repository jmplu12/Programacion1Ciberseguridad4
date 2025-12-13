#4. Crea una clase llamada **CuentaBancaria** con atributos titular y balance. 
# Implementa funciones para depositar y retirar.
class CuentaBancaria:
    def __init__(self, titular: str, balance: float = 0.0):
        self.titular = titular
        self.balance = balance      

    def depositar(self, cantidad: float) -> None:
        """Deposita una cantidad al balance de la cuenta."""
        if cantidad > 0:
            self.balance += cantidad
            print(f"Depósito exitoso: {cantidad}. Nuevo balance: {self.balance}")
        else:
            print("La cantidad a depositar debe ser positiva.")     
    def retirar(self, cantidad: float) -> None:
        """Retira una cantidad del balance de la cuenta si hay fondos suficientes."""
        if cantidad > 0:
            if cantidad <= self.balance:
                self.balance -= cantidad
                print(f"Retiro exitoso: {cantidad}. Nuevo balance: {self.balance}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser positiva.")   
    def solicitar_depositar(self) -> None:
        """Pide al usuario una cantidad por teclado y la deposita si es válida."""
        while True:
            entrada = input("Ingrese cantidad a depositar (o 'cancelar' para volver): ").strip()
            if entrada.lower() == 'cancelar':
                print("Depósito cancelado.")
                return
            try:
                cantidad = float(entrada)
                self.depositar(cantidad)
                return
            except ValueError:
                print("Entrada inválida. Ingrese un número válido (ej: 150.50) o 'cancelar'.")

    def solicitar_retirar(self) -> None:
        """Pide al usuario una cantidad por teclado y la retira si es válida."""
        while True:
            entrada = input("Ingrese cantidad a retirar (o 'cancelar' para volver): ").strip()
            if entrada.lower() == 'cancelar':
                print("Retiro cancelado.")
                return
            try:
                cantidad = float(entrada)
                self.retirar(cantidad)
                return
            except ValueError:
                print("Entrada inválida. Ingrese un número válido (ej: 200) o 'cancelar'.")

    def mostrar_balance(self) -> None:
        print(f"Titular: {self.titular} - Balance actual: {self.balance}")


def menu_interactivo():
    """Menú interactivo para operar con una cuenta bancaria desde teclado."""
    print("--- Menú Cuenta Bancaria ---")
    titular = input("Ingrese el nombre del titular de la cuenta: ").strip()
    # Pedir balance inicial
    while True:
        entrada = input("Ingrese balance inicial (deje vacío para 0): ").strip()
        if entrada == '':
            balance = 0.0
            break
        try:
            balance = float(entrada)
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número para el balance inicial o deje vacío.")

    cuenta = CuentaBancaria(titular, balance)

    acciones = {
        '1': ('Depositar', cuenta.solicitar_depositar),
        '2': ('Retirar', cuenta.solicitar_retirar),
        '3': ('Mostrar balance', cuenta.mostrar_balance),
        '4': ('Salir', None),
    }

    while True:
        print('\nSeleccione una acción:')
        for k, v in acciones.items():
            print(f"{k}. {v[0]}")
        opcion = input('Opción: ').strip()
        if opcion == '4':
            print('Saliendo. Gracias.')
            break
        accion = acciones.get(opcion)
        if accion is None:
            print('Opción inválida. Intente de nuevo.')
            continue
        # Ejecutar la función asociada
        funcion = accion[1]
        if funcion:
            funcion()


if __name__ == '__main__':
    menu_interactivo()
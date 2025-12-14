#    1. Crea una ventana básica con Tkinter que muestre un mensaje de bienvenida usando un Label.
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana de Bienvenida")
ventana.geometry("300x150")

# Crear y colocar el Label con el mensaje de bienvenida
label_bienvenida = tk.Label(ventana, text="¡Bienvenido a la aplicación Tkinter!")
label_bienvenida.pack(pady=20)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()




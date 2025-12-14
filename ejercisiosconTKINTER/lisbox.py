#    4. Crea una ventana con un Listbox que muestre una lista de elementos. Agrega un botón para añadir nuevos elementos a la lista.
import tkinter as tk
from tkinter import simpledialog, messagebox        
# Función para añadir un nuevo elemento al Listbox
def agregar_elemento():
    nuevo_elemento = simpledialog.askstring("Agregar Elemento", "Ingrese el nuevo elemento:")
    if nuevo_elemento:
        listbox.insert(tk.END, nuevo_elemento)
    else:
        messagebox.showwarning("Entrada Vacía", "No se ingresó ningún elemento.")   
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Elementos")
ventana.geometry("300x400") 
# Crear el Listbox  
listbox = tk.Listbox(ventana)
listbox.pack(pady=20, fill=tk.BOTH, expand=True)
# Botón para añadir nuevos elementos
boton_agregar = tk.Button(ventana, text="Agregar Elemento", command=agregar_elemento)
boton_agregar.pack(pady=10)
# Iniciar el bucle principal de la interfaz
ventana.mainloop()
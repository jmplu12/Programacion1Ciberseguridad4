import tkinter as tk
from tkinter import messagebox

def sumar_numeros():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

ventana = tk.Tk()
ventana.title("Calculadora Sencilla")
ventana.geometry("300x200")

label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)

label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar_numeros)
boton_sumar.pack(pady=20)
ventana.bind("<Return>", lambda event: sumar_numeros())

ventana.mainloop()

